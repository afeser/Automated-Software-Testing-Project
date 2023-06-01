# TODO: I started this one, but this took huge amount of time, I'll continue with bottom-up approach and find modules to build

#!/usr/bin/env python
# (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# PYTHON_ARGCOMPLETE_OK

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# ansible.cli needs to be imported first, to ensure the source bin/* scripts run that code first
from ansible.cli import CLI

import os
import sys
import stat

from ansible import constants as C
from ansible import context
from ansible.cli.arguments import option_helpers as opt_help
from ansible.errors import AnsibleError
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.module_utils._text import to_bytes
from ansible.playbook.block import Block
from ansible.plugins.loader import add_all_plugin_dirs
from ansible.utils.collection_loader import AnsibleCollectionConfig
from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path, _get_collection_playbook_path
from ansible.utils.display import Display


import afl
afl.init()

class MockTaskQueueManager:
    RUN_FAILED_BREAK_PLAY = 0
    RUN_FAILED_HOSTS = []
    _failed_hosts = {}
    _unreachable_hosts = {}
    _stats = None

    def __init__(self, *args, **kwargs):
        self.fatih = [{f'my_arg_number_{k}': v for k, v in enumerate(args)}] # list of dictionaries (each call creates a dictionary), first one is always init
        self.fatih[0] = self.fatih[0].update(kwargs) # update the first dictionary with kwargs


    def load_callbacks():
        pass
    def send_callback(self, command: str, *args, **kwargs):
        if 'v2_playbook_on_start' == command:
            self.fatih.append({f'my_arg_number_{k}': v for k, v in enumerate(args)})
            self.fatih[-1] = self.fatih[-1].update(kwargs)

        pass

    def cleanup():
        pass

class MockInventory:
    def get_hosts(hosts, order):
        return []
    def remove_restriction():
        pass
    def restrict_to_hosts(batch):
        pass

class MockVariableManager:
    def get_vars(play):
        return


display = Display()


class PlaybookCLI(CLI):
    ''' the tool to run *Ansible playbooks*, which are a configuration and multinode deployment system.
        See the project home page (https://docs.ansible.com) for more information. '''

    name = 'ansible-playbook'

    def init_parser(self):

        # create parser for CLI options
        super(PlaybookCLI, self).init_parser(
            usage="%prog [options] playbook.yml [playbook2 ...]",
            desc="Runs Ansible playbooks, executing the defined tasks on the targeted hosts.")

        opt_help.add_connect_options(self.parser)
        opt_help.add_meta_options(self.parser)
        opt_help.add_runas_options(self.parser)
        opt_help.add_subset_options(self.parser)
        opt_help.add_check_options(self.parser)
        opt_help.add_inventory_options(self.parser)
        opt_help.add_runtask_options(self.parser)
        opt_help.add_vault_options(self.parser)
        opt_help.add_fork_options(self.parser)
        opt_help.add_module_options(self.parser)

        # ansible playbook specific opts
        self.parser.add_argument('--syntax-check', dest='syntax', action='store_true',
                                 help="perform a syntax check on the playbook, but do not execute it")
        self.parser.add_argument('--list-tasks', dest='listtasks', action='store_true',
                                 help="list all tasks that would be executed")
        self.parser.add_argument('--list-tags', dest='listtags', action='store_true',
                                 help="list all available tags")
        self.parser.add_argument('--step', dest='step', action='store_true',
                                 help="one-step-at-a-time: confirm each task before running")
        self.parser.add_argument('--start-at-task', dest='start_at_task',
                                 help="start the playbook at the task matching this name")
        self.parser.add_argument('args', help='Playbook(s)', metavar='playbook', nargs='+')

    def post_process_args(self, options):

        # for listing, we need to know if user had tag input
        # capture here as parent function sets defaults for tags
        havetags = bool(options.tags or options.skip_tags)

        options = super(PlaybookCLI, self).post_process_args(options)

        if options.listtags:
            # default to all tags (including never), when listing tags
            # unless user specified tags
            if not havetags:
                options.tags = ['never', 'all']

        display.verbosity = options.verbosity
        self.validate_conflicts(options, runas_opts=True, fork_opts=True)

        return options

    def run(self):

        super(PlaybookCLI, self).run()

        # Note: slightly wrong, this is written so that implicit localhost
        # manages passwords
        sshpass = None
        becomepass = None
        passwords = {}

        # initial error check, to make sure all specified playbooks are accessible
        # before we start running anything through the playbook executor
        # also prep plugin paths
        b_playbook_dirs = []
        for playbook in [sys.argv[1]]: #context.CLIARGS['args']:

            # resolve if it is collection playbook with FQCN notation, if not, leaves unchanged
            resource = _get_collection_playbook_path(playbook)
            if resource is not None:
                playbook_collection = resource[2]
            else:
                # not an FQCN so must be a file
                if not os.path.exists(playbook):
                    raise AnsibleError("the playbook: %s could not be found" % playbook)
                if not (os.path.isfile(playbook) or stat.S_ISFIFO(os.stat(playbook).st_mode)):
                    raise AnsibleError("the playbook: %s does not appear to be a file" % playbook)

                # check if playbook is from collection (path can be passed directly)
                playbook_collection = _get_collection_name_from_path(playbook)

            # don't add collection playbooks to adjacency search path
            if not playbook_collection:
                # setup dirs to enable loading plugins from all playbooks in case they add callbacks/inventory/etc
                b_playbook_dir = os.path.dirname(os.path.abspath(to_bytes(playbook, errors='surrogate_or_strict')))
                add_all_plugin_dirs(b_playbook_dir)
                b_playbook_dirs.append(b_playbook_dir)

        if b_playbook_dirs:
            # allow collections adjacent to these playbooks
            # we use list copy to avoid opening up 'adjacency' in the previous loop
            AnsibleCollectionConfig.playbook_paths = b_playbook_dirs

        # don't deal with privilege escalation or passwords when we don't need to
        if not (context.CLIARGS['listhosts'] or context.CLIARGS['listtasks'] or
                context.CLIARGS['listtags'] or context.CLIARGS['syntax']):
            (sshpass, becomepass) = self.ask_passwords()
            passwords = {'conn_pass': sshpass, 'become_pass': becomepass}

        # create base objects
        loader, inventory, variable_manager = self._play_prereqs()

        # (which is not returned in list_hosts()) is taken into account for
        # warning if inventory is empty.  But it can't be taken into account for
        # checking if limit doesn't match any hosts.  Instead we don't worry about
        # limit if only implicit localhost was in inventory to start with.
        #
        # Fix this when we rewrite inventory by making localhost a real host (and thus show up in list_hosts())
        CLI.get_host_list(inventory, context.CLIARGS['subset'])

        # flush fact cache if requested
        if context.CLIARGS['flush_cache']:
            self._flush_cache(inventory, variable_manager)

        # create the playbook executor, which manages running the plays via a task queue manager
        pbex = PlaybookExecutor(playbooks=context.CLIARGS['args'], inventory=inventory,
                                variable_manager=variable_manager, loader=loader,
                                passwords=passwords)
        pbex._tqm = MockTaskQueueManager()

        results = pbex.run()

    @staticmethod
    def _flush_cache(inventory, variable_manager):
        for host in inventory.list_hosts():
            hostname = host.get_name()
            variable_manager.clear_facts(hostname)


def main(args=None):
    PlaybookCLI.cli_executor(args)


if __name__ == '__main__':
    main()

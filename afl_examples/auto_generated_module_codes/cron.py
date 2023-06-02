"""
This file simulates the execution of Ansible.
"""
import sys
sys.path.append('/home/afeser/Automated-Software-Testing-Project/ansible2/test/')

from units.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args
from ansible.module_utils import basic
from units.compat.mock import patch
from ansible.modules import cron


def test_cron(vars):
    if len(vars) != 11:
        return
    
    def get_bin_path(*args, **kwargs):
        return "/usr/sbin/hasan"


    def get_iptables_version(iptables_path, module):
        return "1.8.2"

    mock_get_bin_path = patch.object(basic.AnsibleModule, 'get_bin_path', get_bin_path)
    mock_get_bin_path.start()
    # mock_get_iptables_version = patch.object(cron, 'get_cron_version', get_iptables_version)
    # mock_get_iptables_version.start()
    
    # AUTO GENERATED CODE START -----------------------------------------------------------------
    temp_args ={
        'cron_file': vars[0],
        'env': vars[1],
        'hour': vars[2],
        'insertafter': vars[3],
        'job': vars[4],
        'minute': vars[5],
        'name': vars[6],
        'special_time': vars[7],
        'state': vars[8],
        'user': vars[9],
        'weekday': vars[10],
    }
    remove_keys = []
    for key in temp_args:
        if temp_args[key] == '':
            remove_keys.append(key)
    for key in remove_keys:
        del temp_args[key]
    set_module_args(temp_args)
    # AUTO GENERATED CODE END -------------------------------------------------------------------

    commands_results = [
        (0, '', '') for x in range(100)
    ]

    with patch.object(basic.AnsibleModule, 'run_command') as run_command:
        run_command.side_effect = commands_results
        try:
            cron.main()
        except AnsibleExitJson as result:
            print(result)


    
    mock_get_bin_path.stop()
    # mock_get_iptables_version.stop()

    print('Successfully executed until the end')

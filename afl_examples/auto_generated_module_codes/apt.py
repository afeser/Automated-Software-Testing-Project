"""
This file simulates the execution of Ansible.
"""
import sys
sys.path.append('/home/afeser/Automated-Software-Testing-Project/ansible2/test/')

from units.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args
from ansible.module_utils import basic
from units.compat.mock import patch
from ansible.modules import apt


def test_apt(vars):
    if len(vars) != 12:
        return
    
    def get_bin_path(*args, **kwargs):
        return "/usr/sbin/hasan"


    def get_iptables_version(iptables_path, module):
        return "1.8.2"

    mock_get_bin_path = patch.object(basic.AnsibleModule, 'get_bin_path', get_bin_path)
    mock_get_bin_path.start()
    # mock_get_iptables_version = patch.object(apt, 'get_apt_version', get_iptables_version)
    # mock_get_iptables_version.start()
    
    # AUTO GENERATED CODE START -----------------------------------------------------------------
    temp_args ={
        'autoclean': vars[0],
        'autoremove': vars[1],
        'cache_valid_time': vars[2],
        'deb': vars[3],
        'default_release': vars[4],
        'dpkg_options': vars[5],
        'install_recommends': vars[6],
        'name': vars[7],
        'pkg': vars[8],
        'state': vars[9],
        'update_cache': vars[10],
        'upgrade': vars[11],
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
            apt.main()
        except AnsibleExitJson as result:
            print(result)

        # run_command.return_value = 0, '', ''  # successful execution, no output
        # with self.assertRaises(AnsibleExitJson) as result:
        
            # self.assertTrue(result.exception.args[0]['changed'])


    mock_get_bin_path.stop()
    # mock_get_iptables_version.stop()

    print('Successfully executed until the end')

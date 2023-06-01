"""
This file simulates the execution of Ansible.
"""
import sys
sys.path.append('/home/afeser/Automated-Software-Testing-Project/ansible2/test/')

from units.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args
from ansible.module_utils import basic
from units.compat.mock import patch
from ansible.modules import iptables


def test_iptables(vars):
    if len(vars) != 28:
        return
    
    def get_bin_path(*args, **kwargs):
        return "/usr/sbin/hasan"


    def get_iptables_version(iptables_path, module):
        return "1.8.2"

    mock_get_bin_path = patch.object(basic.AnsibleModule, 'get_bin_path', get_bin_path)
    mock_get_bin_path.start()
    mock_get_iptables_version = patch.object(iptables, 'get_iptables_version', get_iptables_version)
    mock_get_iptables_version.start()
    
    # AUTO GENERATED CODE START -----------------------------------------------------------------
    temp_args ={
        'action': vars[0],
        'chain': vars[1],
        'comment': vars[2],
        'ctstate': vars[3],
        'destination_port': vars[4],
        'dst_range': vars[5],
        'flush': vars[6],
        'in_interface': vars[7],
        'ip_version': vars[8],
        'jump': vars[9],
        'limit': vars[10],
        'limit_burst': vars[11],
        'log_level': vars[12],
        'log_prefix': vars[13],
        'match': vars[14],
        'policy': vars[15],
        'protocol': vars[16],
        'reject_with': vars[17],
        'rule_num': vars[18],
        'set_dscp_mark': vars[19],
        'set_dscp_mark_class': vars[20],
        'source': vars[21],
        'src_range': vars[22],
        'state': vars[23],
        'syn': vars[24],
        'table': vars[25],
        'tcp_flags': vars[26],
        'to_ports': vars[27],
    }
    remove_keys = []
    for key in temp_args:
        if temp_args[key] == '':
            remove_keys.append(key)
    for key in remove_keys:
        del temp_args[key]
    
    print('setting args', temp_args)
    set_module_args(temp_args)
    # AUTO GENERATED CODE END -------------------------------------------------------------------

    commands_results = [
        (0, '', ''),
    ]

    with patch.object(basic.AnsibleModule, 'run_command') as run_command:
        run_command.side_effect = commands_results
        try:
            iptables.main()
        except AnsibleExitJson as result:
            print(result)

        # run_command.return_value = 0, '', ''  # successful execution, no output
        # with self.assertRaises(AnsibleExitJson) as result:
        
            # self.assertTrue(result.exception.args[0]['changed'])


    mock_get_bin_path.stop()
    mock_get_iptables_version.stop()
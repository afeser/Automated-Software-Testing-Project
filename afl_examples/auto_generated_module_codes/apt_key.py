"""
This file simulates the execution of Ansible.
"""
import sys
sys.path.append('/home/afeser/Automated-Software-Testing-Project/ansible2/test/')

from units.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args
from ansible.module_utils import basic
from units.compat.mock import patch
from ansible.modules import apt_key


def test_apt_key(vars):
    if len(vars) != 7:
        return
    
    def get_bin_path(*args, **kwargs):
        return "/usr/sbin/hasan"


    def get_iptables_version(iptables_path, module):
        return "1.8.2"

    mock_get_bin_path = patch.object(basic.AnsibleModule, 'get_bin_path', get_bin_path)
    mock_get_bin_path.start()
    # mock_get_iptables_version = patch.object(apt_key, 'get_apt_key_version', get_iptables_version)
    # mock_get_iptables_version.start()
    
        # AUTO GENERATED CODE START -----------------------------------------------------------------
    temp_args ={
        'data': vars[0],
        'file': vars[1],
        'id': vars[2],
        'keyring': vars[3],
        'keyserver': vars[4],
        'state': vars[5],
        'url': vars[6],
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
        (0, """
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
Executing: /tmp/apt-key-gpghome.bbTWyeyEz2/gpg.1.sh --list-public-keys --keyid-format=long
/tmp/apt-key-gpghome.bbTWyeyEz2/pubring.gpg
-------------------------------------------
pub   rsa4096/D94AA3F0EFE21092 2012-05-11 [SC]
      843938DF228D22F7B3742BC0D94AA3F0EFE21092
uid                 [ unknown] Ubuntu CD Image Automatic Signing Key (2012) <cdimage@ubuntu.com>

pub   rsa4096/871920D1991BC93C 2018-09-17 [SC]
      F6ECB3762474EDA9D21B7022871920D1991BC93C
uid                 [ unknown] Ubuntu Archive Automatic Signing Key (2018) <ftpmaster@ubuntu.com>


""", '') for x in range(100)
    ]

    with patch.object(basic.AnsibleModule, 'run_command') as run_command:
        run_command.side_effect = commands_results
        try:
            apt_key.main()
        except AnsibleExitJson as result:
            print(result)

        # run_command.return_value = 0, '', ''  # successful execution, no output
        # with self.assertRaises(AnsibleExitJson) as result:
        
            # self.assertTrue(result.exception.args[0]['changed'])


    mock_get_bin_path.stop()
    # mock_get_iptables_version.stop()

    print('Successfully executed until the end')

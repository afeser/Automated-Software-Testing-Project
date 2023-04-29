# Default Core Modules Coverage
Testing all core modules are done by `ansible-test units --coverage apt --docker`.


<details>
  <summary>Coverage result:</summary>
  Name                                                                           Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------------------------------------------------------
lib/ansible/module_utils/__init__.py                                               0      0      0      0   100%
lib/ansible/module_utils/_text.py                                                  6      0      0      0   100%
lib/ansible/module_utils/basic.py                                               1216   1044    555      1    11%
lib/ansible/module_utils/common/__init__.py                                        0      0      0      0   100%
lib/ansible/module_utils/common/_json_compat.py                                    9      3      2      1    64%
lib/ansible/module_utils/common/_utils.py                                         14     10      8      0    18%
lib/ansible/module_utils/common/arg_spec.py                                      120     98     34      0    18%
lib/ansible/module_utils/common/collections.py                                    52     33     14      0    29%
lib/ansible/module_utils/common/file.py                                           28      8      4      0    62%
lib/ansible/module_utils/common/locale.py                                         29     25     16      0     9%
lib/ansible/module_utils/common/parameters.py                                    448    411    316      0     5%
lib/ansible/module_utils/common/process.py                                        26     21     16      0    12%
lib/ansible/module_utils/common/respawn.py                                        38     28     10      0    21%
lib/ansible/module_utils/common/sys_info.py                                       60     50     40      0    10%
lib/ansible/module_utils/common/text/__init__.py                                   0      0      0      0   100%
lib/ansible/module_utils/common/text/converters.py                               112     90     74      0    13%
lib/ansible/module_utils/common/text/formatters.py                                57     49     27      0    10%
lib/ansible/module_utils/common/validation.py                                    263    231    174      0     7%
lib/ansible/module_utils/common/warnings.py                                       19     10      6      0    36%
lib/ansible/module_utils/compat/__init__.py                                        0      0      0      0   100%
lib/ansible/module_utils/compat/_selectors2.py                                   411    333    158      9    15%
lib/ansible/module_utils/compat/selectors.py                                      17      0      2      0   100%
lib/ansible/module_utils/compat/selinux.py                                        62     29     15      2    55%
lib/ansible/module_utils/compat/typing.py                                         15      5      0      0    67%
lib/ansible/module_utils/distro/__init__.py                                       16      3      4      1    70%
lib/ansible/module_utils/distro/_distro.py                                       335    231    134      3    27%
lib/ansible/module_utils/errors.py                                                46     13      8      0    72%
lib/ansible/module_utils/parsing/__init__.py                                       0      0      0      0   100%
lib/ansible/module_utils/parsing/convert_bool.py                                  18     10     10      0    29%
lib/ansible/module_utils/pycompat24.py                                             7      1      0      0    86%
lib/ansible/module_utils/six/__init__.py                                         505    185    166      9    58%
lib/ansible/module_utils/urls.py                                                1048    866    414      5    13%
lib/ansible/modules/__init__.py                                                    0      0      0      0   100%
lib/ansible/modules/apt.py                                                       639    554    328      5    10%
test/lib/ansible_test/_util/target/pytest/plugins/ansible_forked.py               55     23     26      2    49%
test/lib/ansible_test/_util/target/pytest/plugins/ansible_pytest_coverage.py      44     16     18      5    60%
test/units/__init__.py                                                             0      0      0      0   100%
test/units/compat/__init__.py                                                      0      0      0      0   100%
test/units/compat/mock.py                                                          6      0      0      0   100%
test/units/compat/unittest.py                                                      5      0      2      0   100%
test/units/modules/__init__.py                                                     0      0      0      0   100%
test/units/modules/conftest.py                                                    21     12     12      0    33%
test/units/modules/test_apt.py                                                    29      3      2      0    84%
----------------------------------------------------------------------------------------------------------------
TOTAL                                                                           5776   4395   2595     43    19%

  
</details>

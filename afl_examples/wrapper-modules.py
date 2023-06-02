"""
One wrapper for all the source files.
This one just reads the input line by line and feeds the arguments to the target functions defined in this file.

Run this with:
source ~/Automated-Software-Testing-Project/ansible2/hacking/env-setup && mkdir -p outputs && py-afl-fuzz -m 400 -i inputs/find.pfilter/ -o outputs/find.pfilter/ -- python3 wrapper-modules.py @@
"""
from ansible.modules.find import pfilter

import os
import sys
from module_adapters.find import pfilter
from auto_generated_module_codes.iptables import test_iptables
from auto_generated_module_codes.apt import test_apt
from auto_generated_module_codes.apt_key import test_apt_key

import afl
afl.init()



# If you overwrite this variable, AFL complains about no instrumentation found
path = sys.argv[1] #sys.stdin.read()


fail = False
number_args = 0
arguments = []
with open(path, 'rb') as f:
    with open('deneme.txt', 'a') as f2:
        while True:
            try:
                new_var = f.readline().decode('utf-8')
                if len(new_var) == 0:
                    break
                f2.write(new_var)
                arguments.append(new_var)
                number_args = number_args + 1
            except UnicodeDecodeError:
                fail = True
    
        f2.write('\n------------------------------------------------\n');

    
# I also realized, if I add os._exit(0) to different places, the code cannot find instrumentation.
# Therefore, you see a lot of if/else blocks

# We are only interested in ascii strings
if not fail:
    if new_var.isascii():
        # pfilter(arguments)
        arguments = [arg.rstrip() for arg in arguments]
        print('Number arguments', number_args)

        # I add if statement here because this is controlled by a bash script
        # I don't want to mess up output folders by supplying `iptables` binary to `apt` inputs/ouputs for example
        # Therefore, please add new tests here
        if sys.argv[2] == 'apt':
            test_apt(arguments)
        elif sys.argv[2] == 'iptables':
            test_iptables(arguments)
        elif sys.argv[2] == 'apt_key':
            test_apt_key(arguments)
        else:
            print('Nothing to do!')

        

    


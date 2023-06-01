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
from iptables_simulation_script import test_iptables

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
        test_iptables(arguments)

        

    


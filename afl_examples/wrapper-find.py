"""
Run this with:
source ~/Automated-Software-Testing-Project/ansible2/hacking/env-setup && mkdir -p outputs && py-afl-fuzz -m 400 -i inputs/find.pfilter/ -o outputs/find.pfilter/ -- python3 wrapper-find.py
"""
from ansible.modules.find import pfilter

import os
import sys

import afl
afl.init()

def pfilter(afl_input: str):
    vals = afl_input.split('\n')
    # 3 arguments
    if len(vals) == 3:
        patterns, excludes, use_regex = vals[0], vals[1], vals[2]

        if use_regex == 'yes':
            use_regex = True
            pfilter(patterns, excludes, use_regex)
        elif use_regex == 'no':
            use_regex = False
            pfilter(patterns, excludes, use_regex)



# If you overwrite this variable, AFL complains about no instrumentation found
path = sys.argv[1] #sys.stdin.read()

with open(path, 'rb') as f:
    try:
        new_var = f.read().decode('utf-8')
    except UnicodeDecodeError:
        os._exit(0)
    
# I also realized, if I add os._exit(0) to different places, the code cannot find instrumentation.
# Therefore, you see a lot of if/else blocks

# We are only interested in ascii strings
if new_var.isascii():
    pfilter(new_var)

        

    


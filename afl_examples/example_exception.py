#!/usr/bin/python3
import os
import sys

def exception_if_input_is_42(x):
    if x == 42:
        raise Exception("Input is 42!")
    print(f'Input is {x}')
    return x




import afl
afl.init()

sys.stdin.seek(0)
# exception_if_input_is_42(sys.stdin.read())

os._exit(0)

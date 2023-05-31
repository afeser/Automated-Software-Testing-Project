"""
Command to run this: py-afl-fuzz -m 400 -i initial-inputs/ -o fuzzing-results/ -- python3 fuzz-wrapper.py
You can read from file (but slower and need to change this program): py-afl-fuzz -m 400 -i initial-inputs/ -o fuzzing-results/ -- python3 fuzz-wrapper.py @@
"""
# import os
import sys

import afl
afl.init()


path = sys.stdin.read()


# path = 'deneme.txt'
# user_in = b'empty :/'
# with open(path, 'rb') as f:    
#     avs = f.read()


# Print outputs if you wish (to see how it behaves)
# with open('inputs_to_file.txt', 'a') as f:
#     f.write(path)
#     f.write('\n')

if 'hamsi' in path:
    raise Exception('My exception')

# os._exit(0)

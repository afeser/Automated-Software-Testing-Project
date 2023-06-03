#!/usr/bin/python3
import sys
import os
import time

cmd_compile = '/home/afeser/Automated-Software-Testing-Project/sym/a/clang_compile.sh'

with open('/home/afeser/Automated-Software-Testing-Project/sym/a/script_output.txt', 'a') as f:
    f.write(f'{time.time()} - All input flags:' + ' '.join(sys.argv) + '\n')

with open(cmd_compile, 'a') as f:
    # -emit-llvm -c -g -O0 -Xclang -disable-O0-optnone 
    f.write(f'/usr/bin/clang -emit-llvm ' + ' '.join(sys.argv[1:]) + '\n')
os.system(f'chmod +x {cmd_compile}') 



#!/usr/bin/python3
import sys
import os
import time

cmd_compile = '/home/afeser/Automated-Software-Testing-Project/sym/a/clang_compile.sh'

with open('/home/afeser/Automated-Software-Testing-Project/sym/a/script_output.txt', 'a') as f:
    f.write(f'{time.time()} - All input flags:' + ' '.join(sys.argv) + '\n')

with open(cmd_compile, 'a') as f:
    # -emit-llvm -c -g -O0 -Xclang -disable-O0-optnone 
    # from coreutils tutorial: -g -O1 -Xclang -disable-llvm-passes -D__NO_STRING_INLINES  -D_FORTIFY_SOURCE=0 -U__OPTIMIZE__
    cmd = f'/usr/bin/clang-11 -c -emit-llvm -g -O1 -Xclang -disable-llvm-passes -D__NO_STRING_INLINES  -D_FORTIFY_SOURCE=0 -U__OPTIMIZE__ ' + ' '.join(sys.argv[1:]).replace('.o', '.bc') + '\n'
    f.write('echo ' + cmd)
    f.write(cmd)
os.system(f'chmod +x {cmd_compile}') 



# Symbolic Execution

In this directory, you can find `deneme.py` which is a simple python script to be tested for symbolic execution.
`deneme.build` directory includes the converted C files created by Nuitka.
These files are compiled with script `clang_compile.sh`.
Please note that this script is automatically generated by `script.py` after calling Nuitka with only compile mode, no C code generation mode.
Please relink your compiler so that Nuitka calls this script instead of your compiler.
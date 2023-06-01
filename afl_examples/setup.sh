# Kill upon error
set -e

# Install AFL
git clone https://github.com/mirrorer/afl.git
cd afl
make && sudo make install
cd ..

git clone https://github.com/jwilk/python-afl.git
pip3 install Cython
cd python-afl
python3 setup.py build
mkdir install_dir
python3 setup.py install --prefix install_dir
echo 'export PATH=$PATH:'"$(pwd)/install_dir/bin" >> ~/.bashrc



echo "DONE!"
module_name=apt

echo "Starting fuzzer 1"
tmux new-session -d -s $module_name.01master "py-afl-fuzz -m 5000  -i ./inputs/$module_name/inputs -o outputs/$module_name -M fuzzer01 -- python3 ./wrapper-modules.py  @@ $module_name"
sleep 1
echo "Starting fuzzer 2"
tmux new-session -d -s $module_name.02slave "py-afl-fuzz -m 5000  -i ./inputs/$module_name/inputs -o outputs/$module_name -S fuzzer02 -- python3 ./wrapper-modules.py  @@ $module_name"
sleep 1
echo "Starting fuzzer 3"
tmux new-session -d -s $module_name.03slave "py-afl-fuzz -m 5000  -i ./inputs/$module_name/inputs -o outputs/$module_name -S fuzzer03 -- python3 ./wrapper-modules.py  @@ $module_name"
sleep 1
echo "Starting fuzzer 4"
tmux new-session -d -s $module_name.04slave "py-afl-fuzz -m 5000  -i ./inputs/$module_name/inputs -o outputs/$module_name -S fuzzer04 -- python3 ./wrapper-modules.py  @@ $module_name"


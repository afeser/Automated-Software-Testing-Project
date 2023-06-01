echo "Startin fuzzer 1"
tmux new-session -d -s 01master "py-afl-fuzz -m 5000  -i ./inputs/iptables/inputs -o outputs/iptables -M fuzzer01 -- python3 ./wrapper-modules.py  @@"
sleep 1
echo "Startin fuzzer 2"
tmux new-session -d -s 02slave "py-afl-fuzz -m 5000  -i ./inputs/iptables/inputs -o outputs/iptables -S fuzzer02 -- python3 ./wrapper-modules.py  @@"
sleep 1
echo "Startin fuzzer 3"
tmux new-session -d -s 03slave "py-afl-fuzz -m 5000  -i ./inputs/iptables/inputs -o outputs/iptables -S fuzzer03 -- python3 ./wrapper-modules.py  @@"
sleep 1
echo "Startin fuzzer 4"
tmux new-session -d -s 04slave "py-afl-fuzz -m 5000  -i ./inputs/iptables/inputs -o outputs/iptables -S fuzzer04 -- python3 ./wrapper-modules.py  @@"


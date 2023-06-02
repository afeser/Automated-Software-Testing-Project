module_name=iptables
num_cores=4

# start master anyway...
tmux new-session -d -s $module_name.01master "source /home/afeser/.bashrc; source ~/Automated-Software-Testing-Project/ansible2/hacking/env-setup; py-afl-fuzz -t 10000 -m 5000  -i ./inputs/$module_name/inputs -o outputs/$module_name -M fuzzer0 -- python3 ./wrapper-modules.py  @@ $module_name"
sleep 1

end=$(($num_cores-1))
start=1 
# start slaves
for (( i=$start; i<=$end; i++ ))
do
    echo "Starting fuzzer $i"
    tmux new-session -d -s $module_name.$i.slave "source /home/afeser/.bashrc; source ~/Automated-Software-Testing-Project/ansible2/hacking/env-setup; py-afl-fuzz -t 10000 -m 5000  -i ./inputs/$module_name/inputs -o outputs/$module_name -S fuzzer$i -- python3 ./wrapper-modules.py  @@ $module_name"
    sleep 1
done


# echo "Starting fuzzer 2"
# tmux new-session -d -s $module_name.02slave "py-afl-fuzz -m 5000  -i ./inputs/$module_name/inputs -o outputs/$module_name -S fuzzer02 -- python3 ./wrapper-modules.py  @@ $module_name"
# sleep 1
# echo "Starting fuzzer 3"
# tmux new-session -d -s $module_name.03slave "py-afl-fuzz -m 5000  -i ./inputs/$module_name/inputs -o outputs/$module_name -S fuzzer03 -- python3 ./wrapper-modules.py  @@ $module_name"
# sleep 1
# echo "Starting fuzzer 4"
# tmux new-session -d -s $module_name.04slave "py-afl-fuzz -m 5000  -i ./inputs/$module_name/inputs -o outputs/$module_name -S fuzzer04 -- python3 ./wrapper-modules.py  @@ $module_name"



vms="VM1 VM2 VM3 VM4"

port=2022
wait_time=60 # need to wait more for the next machines...
for vm in $vms
do
	echo "Starting virtual machine $vm"
	VBoxManage modifyvm $vm --natpf1 "guestssh,tcp,,$port,,22"
	echo "Forwarded port 22 of VM to port $port of the host machine"
	port=$(($port+1))
	VBoxManage modifyvm $vm --defaultfrontend headless
	VBoxHeadless --startvm $vm &
	echo "Waiting $wait_time seconds before starting the next one"
	sleep $wait_time
	wait_time=$(($wait_time+60))
done

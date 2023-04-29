module_names="apt_key async_wrapper hostname known_hosts service_facts systemd yum apt copy iptables pip service unarchive utils"

report_file=/home/afeser/ansible2/test/results/reports/coverage/index.html

for test in $module_names
do
    if [ -z "coverage_result_$test.html" ]
    then
        echo "Found already an existing result. Please remove it first if you wish to run again: coverage_result_$test.html"
    else
        echo "Running tests for $test"
        ansible-test coverage erase
        ansible-test units --coverage $test --docker
        ansible-test coverage html
        mv $report_file coverage_result_$test.html
    fi

done
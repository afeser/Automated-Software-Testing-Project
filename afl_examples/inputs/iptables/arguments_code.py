# AUTO GENERATED CODE START -----------------------------------------------------------------
temp_args ={
	'action': vars[0],
	'chain': vars[1],
	'comment': vars[2],
	'ctstate': vars[3],
	'destination_port': vars[4],
	'dst_range': vars[5],
	'flush': vars[6],
	'in_interface': vars[7],
	'ip_version': vars[8],
	'jump': vars[9],
	'limit': vars[10],
	'limit_burst': vars[11],
	'log_level': vars[12],
	'log_prefix': vars[13],
	'match': vars[14],
	'policy': vars[15],
	'protocol': vars[16],
	'reject_with': vars[17],
	'rule_num': vars[18],
	'set_dscp_mark': vars[19],
	'set_dscp_mark_class': vars[20],
	'source': vars[21],
	'src_range': vars[22],
	'state': vars[23],
	'syn': vars[24],
	'table': vars[25],
	'tcp_flags': vars[26],
	'to_ports': vars[27],
}
remove_keys = []
for key in temp_args:
	if temp_args[key] == '':
		remove_keys.append(key)
for key in remove_keys:
	del temp_args[key]
set_module_args(temp_args)
# AUTO GENERATED CODE END -------------------------------------------------------------------

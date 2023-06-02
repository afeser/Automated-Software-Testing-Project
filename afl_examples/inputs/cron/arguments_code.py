    # AUTO GENERATED CODE START -----------------------------------------------------------------
    temp_args ={
        'cron_file': vars[0],
        'env': vars[1],
        'hour': vars[2],
        'insertafter': vars[3],
        'job': vars[4],
        'minute': vars[5],
        'name': vars[6],
        'special_time': vars[7],
        'state': vars[8],
        'user': vars[9],
        'weekday': vars[10],
    }
    remove_keys = []
    for key in temp_args:
        if temp_args[key] == '':
            remove_keys.append(key)
    for key in remove_keys:
        del temp_args[key]
    set_module_args(temp_args)
    # AUTO GENERATED CODE END -------------------------------------------------------------------

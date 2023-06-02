    # AUTO GENERATED CODE START -----------------------------------------------------------------
    temp_args ={
        'daemon_reexec': vars[0],
        'daemon_reload': vars[1],
        'enabled': vars[2],
        'masked': vars[3],
        'name': vars[4],
        'state': vars[5],
    }
    remove_keys = []
    for key in temp_args:
        if temp_args[key] == '':
            remove_keys.append(key)
    for key in remove_keys:
        del temp_args[key]
    set_module_args(temp_args)
    # AUTO GENERATED CODE END -------------------------------------------------------------------

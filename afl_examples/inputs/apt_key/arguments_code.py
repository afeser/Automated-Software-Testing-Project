    # AUTO GENERATED CODE START -----------------------------------------------------------------
    temp_args ={
        'data': vars[0],
        'file': vars[1],
        'id': vars[2],
        'keyring': vars[3],
        'keyserver': vars[4],
        'state': vars[5],
        'url': vars[6],
    }
    remove_keys = []
    for key in temp_args:
        if temp_args[key] == '':
            remove_keys.append(key)
    for key in remove_keys:
        del temp_args[key]
    set_module_args(temp_args)
    # AUTO GENERATED CODE END -------------------------------------------------------------------

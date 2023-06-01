    # AUTO GENERATED CODE START -----------------------------------------------------------------
    temp_args ={
        'autoclean': vars[0],
        'autoremove': vars[1],
        'cache_valid_time': vars[2],
        'deb': vars[3],
        'default_release': vars[4],
        'dpkg_options': vars[5],
        'install_recommends': vars[6],
        'name': vars[7],
        'pkg': vars[8],
        'state': vars[9],
        'update_cache': vars[10],
        'upgrade': vars[11],
    }
    remove_keys = []
    for key in temp_args:
        if temp_args[key] == '':
            remove_keys.append(key)
    for key in remove_keys:
        del temp_args[key]
    set_module_args(temp_args)
    # AUTO GENERATED CODE END -------------------------------------------------------------------

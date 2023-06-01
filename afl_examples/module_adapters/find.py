
def pfilter(vals: str):
    # 3 arguments
    if len(vals) == 3:
        patterns, excludes, use_regex = vals[0], vals[1], vals[2]

        if use_regex == 'yes':
            use_regex = True
            pfilter(patterns, excludes, use_regex)
        elif use_regex == 'no':
            use_regex = False
            pfilter(patterns, excludes, use_regex)

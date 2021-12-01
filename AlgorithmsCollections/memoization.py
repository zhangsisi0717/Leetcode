def cache(f):
    res_dict = {}
    def _f(arg1, arg2):
        if (arg1, arg2) not in res_dict:
            res_dict[(arg1, arg2)] = f(arg)
        return res_dict[(arg1, arg2)]
    return _f
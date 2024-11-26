def apply_all_func(int_list:list, *functions):
    types = [float,int]
    try :
        for i in int_list:
            if type(i) not in types:
                return 'Параметр int_list должен содержать только числа.'
    except TypeError:
        return 'Параметр int_list должен быть списком.'
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max,min))
print(apply_all_func([6, 20, 15, 9], len,sum, sorted))
print(apply_all_func(5, len,sum))
print(apply_all_func('apple', len))
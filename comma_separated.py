def get_string(some_list):
    some_list[-1] = 'and ' + some_list[-1]
    return ', '.join(some_list)


lst = input('>>> ').split(' ')

print(get_string(lst))

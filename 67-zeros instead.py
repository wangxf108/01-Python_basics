lst = [99, 'no data', 95, 94, 'no data']
def foo(lst):
    new_lst = [i for i in lst if  isinstance(i, int)]

print(new_lst)


def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]       #isinstance(i, int) 指定类型，遇到了很多次
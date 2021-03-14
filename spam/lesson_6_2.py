import sys


def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)


show(42)

lst = [i for i in range(12)]
show(lst)
print('*' * 50)
show(tuple(lst))
print('*' * 50)
show(set(lst))
print('*' * 50)
show({f'{i}': i for i in range(10)})
# show({i: i for i in range(10)})
show('Hello')

import sys
# import random


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


def memory_sum(obj):
    sum_ = 0
    sum_ += sys.getsizeof(obj)

    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                sum_ += memory_sum(key)
                sum_ += memory_sum(value)
        elif not isinstance(obj, str):
            for item in obj:
                sum_ += memory_sum(item)
    return sum_


# 3. Попробую tuple вместо list и генератор для second
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

# first = {i: random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)}
first = {0: 16, 1: 22, 2: 45, 3: 95, 4: 76, 5: 89, 6: 60, 7: 2, 8: 13, 9: 25}
second = tuple(first[i] for i in first.keys() if first[i] % 2 == 0)

lst = SIZE, MIN_ITEM, MAX_ITEM, first, second
res = 0

for i in lst:
    res += memory_sum(i)

print('*' * 50)
print(f'Под переменные, \033[34mне считая lst\033[0m (списка с переменными),'
      f'\nбыло выделено \033[91m\033[1m{res} байт\033[0m памяти.')
print('*' * 50)
# print(show(lst))

"""
python 3.8.5
Ubuntu 20.04.2 LTS 64-bit на виртуальной машине
**************************************************
Под переменные, не считая lst (списка с переменными),
было выделено 1216 байт памяти.
**************************************************
"""

"""
**********
 Выводы:
**********
Как и ожидалось второй вариант с tuple легче остальных,
так как не резервирует дополнительные ячейки памяти.

Третий вариант с dict самый ресурсоёмкий из трёх, спасибо хешу.
Также пробовал collections.defaultdictjy, он ест ещё больше 1224 (в третьем примере вместо dict)
"""

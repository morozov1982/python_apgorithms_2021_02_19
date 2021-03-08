"""
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


SIZE = 10
MIN_ITEM = 2
MAX_ITEM = 99
array = [i for i in range(MIN_ITEM, MAX_ITEM + 1)]
# print(array)


FIRST = 2
LAST = 9
dig_sum = {dig: 0 for dig in range(FIRST, LAST + 1)}

for num in array:
    for dig in range(FIRST, LAST + 1):
        if not num % dig:
            dig_sum[dig] += 1

for key in dig_sum:
    print(f'{key} -> {dig_sum[key]}')

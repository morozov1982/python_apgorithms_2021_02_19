"""
4. Определить, какое число в массиве встречается чаще всего.
"""


import random

SIZE = 10  # 10_000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

frequency = {}
frequent_num = 0
occur_times = 0

for el in array:
    if el not in frequency:
        frequency[el] = 1
    else:
        frequency[el] += 1

for val in frequency:
    if frequency[val] > occur_times:
        frequent_num = val
        occur_times = frequency[val]

print(frequency)
print(f'Чаще всего встречается: {frequent_num} - {occur_times} раз')

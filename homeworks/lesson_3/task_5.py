"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""


import random

SIZE = 10  # 10_000
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_negative = None

for i in array:
    if 0 > i:
        if not max_negative or i > max_negative:
            max_negative = i


print(f'Максимальный отрицательный элемент: {max_negative}')

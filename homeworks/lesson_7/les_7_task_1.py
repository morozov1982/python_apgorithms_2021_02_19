"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.

Примечания:
    ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
    ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
      Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
from random import randrange
import timeit

SIZE = 10
FIRST = -100
LAST = 100


# решил сразу сделать универсальную функцию
def bubble_sort(data, reverse=False):
    n = 1
    while n < len(data):
        for i in range(len(data) - 1):
            if not reverse and data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
            elif reverse and data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        n += 1


# оптимизированный вариант
def bubble_sort_opt(data, reverse=False):
    # быстрее 1 раз посчитать, чем в каждом range()
    last = len(data) - 1

    # for немного быстрее while
    for j in range(last):
        # исключаем уже отсортированные элементы
        for i in range(last - j):
            if not reverse and data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
            elif reverse and data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]


arr = [randrange(FIRST, LAST) for _ in range(SIZE)]  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(f'\33[92m\33[1mМассив:\33[0m')
print(arr)

bubble_sort_opt(arr, reverse=True)
print(f'\33[92mОтсортированный \33[1mв обратном порядке:\33[0m')
print(arr)

bubble_sort_opt(arr)
print(f'\33[92m\33[1mНормальная сортировка:\33[0m')
print(arr)


# Раз стоит задача улучшить, значит надо проверить на улучшение ;-)
print(f'\n\33[94mТест скорости для \33[93m\33[1mbubble_sort():\33[0m')
print(timeit.timeit('bubble_sort([randrange(FIRST, LAST) for _ in range(10)], reverse=True)',
                    number=100, globals=globals()))  # 0.005214337999859708
print(timeit.timeit('bubble_sort([randrange(FIRST, LAST) for _ in range(20)], reverse=True)',
                    number=100, globals=globals()))  # 0.018411801000183914
print(timeit.timeit('bubble_sort([randrange(FIRST, LAST) for _ in range(40)], reverse=True)',
                    number=100, globals=globals()))  # 0.06534851700052968
print(timeit.timeit('bubble_sort([randrange(FIRST, LAST) for _ in range(80)], reverse=True)',
                    number=100, globals=globals()))  # 0.22786921300030372
print(timeit.timeit('bubble_sort([randrange(FIRST, LAST) for _ in range(160)], reverse=True)',
                    number=100, globals=globals()))  # 0.8308473990000493

print(f'\n\33[94mТест скорости для \33[93m\33[1mbubble_sort_opt():\33[0m')
print(timeit.timeit('bubble_sort_opt([randrange(FIRST, LAST) for _ in range(10)], reverse=True)',
                    number=100, globals=globals()))  # 0.0036557369985530386
print(timeit.timeit('bubble_sort_opt([randrange(FIRST, LAST) for _ in range(20)], reverse=True)',
                    number=100, globals=globals()))  # 0.010815185998581
print(timeit.timeit('bubble_sort_opt([randrange(FIRST, LAST) for _ in range(40)], reverse=True)',
                    number=100, globals=globals()))  # 0.03662207699926512
print(timeit.timeit('bubble_sort_opt([randrange(FIRST, LAST) for _ in range(80)], reverse=True)',
                    number=100, globals=globals()))  # 0.13310558900047909
print(timeit.timeit('bubble_sort_opt([randrange(FIRST, LAST) for _ in range(160)], reverse=True)',
                    number=100, globals=globals()))  # 0.5032638310003676

# Определённо, после усовершенствований функция работает куда быстрее, (почти в 2 раза)

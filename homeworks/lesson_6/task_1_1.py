"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание:
По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
    ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
    ● написать 3 варианта кода (один у вас уже есть);
    ● проанализировать 3 варианта и выбрать оптимальный;
    ● результаты анализа (количество занятой памяти в вашей среде разработки)
      вставить в виде комментариев в файл с кодом.
      Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
    ● написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
а проявили творчество, фантазию и создали универсальный код для замера памяти.

Взял: lesson_3/task_2.py
"""
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


# 1. Было так:
# import random
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
# first = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
first = [31, 94, 99, 75, 12, 58, 4, 5, 94, 25]  # чтобы результаты не были рандомными ;-)
# print(first)
second = []

for idx, num in enumerate(first):
    if not num % 2:
        second.append(idx)


lst = SIZE, MIN_ITEM, MAX_ITEM, first, second
res = 0

for i in lst:
    res += memory_sum(i)

print('*' * 50)
print(f'Под переменные, \033[34mне считая lst\033[0m (списка с переменными),'
      f'\nбыло выделено \033[93m\033[1m{res} байт\033[0m памяти.')
print('*' * 50)
# print(show(lst))  # можно проверить и пересчитать в ручную, я пересчитывал, всё сходится ;-)

"""
python 3.8.5
Ubuntu 20.04.2 LTS 64-bit на виртуальной машине
**************************************************
Под переменные, не считая lst (списка с переменными),
было выделено 756 байт памяти.
**************************************************
"""

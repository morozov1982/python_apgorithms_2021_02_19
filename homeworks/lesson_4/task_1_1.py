"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.

Примечание. Идеальным решением будет:
    ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
    ● написать 3 варианта кода (один у вас уже есть),
    ● проанализировать 3 варианта и выбрать оптимальный,
    ● результаты анализа вставить в виде комментариев в файл с кодом
      (не забудьте указать, для каких N вы проводили замеры),
    ● написать общий вывод: какой из трёх вариантов лучше и почему.

Взял: lesson_2/task_4
"""
import timeit
import cProfile


# 0. Было решено так:
# def seq_sum(n):
#     tmp = 1
#     summ = 0
#
#     for i in range(n):
#         summ += tmp
#         tmp = -(tmp / 2)
#
#     return summ
#
#
# num = int(input('Введи натуральное число: '))
# s = seq_sum(num)
# print(f'Сумма {num} элементов ряда чисел: 1, -0.5, 0.25, -0.125, ... равна: {s}')


# 1. Немного модернизирую, для красоты и удобства
def seq_sum(n):
    spam = 1
    sum_ = 0

    for _ in range(n):
        sum_ += spam
        spam = -(spam / 2)

    return sum_


print(timeit.timeit('seq_sum(10)', number=100, globals=globals()))      # 0.0002750950006884523
print(timeit.timeit('seq_sum(20)', number=100, globals=globals()))      # 0.0004966339984093793
print(timeit.timeit('seq_sum(40)', number=100, globals=globals()))      # 0.0009943330005626194
print(timeit.timeit('seq_sum(80)', number=100, globals=globals()))      # 0.0018901460025517736
print(timeit.timeit('seq_sum(160)', number=100, globals=globals()))     # 0.0038562230001844
print(timeit.timeit('seq_sum(320)', number=100, globals=globals()))     # 0.009462573998462176
print(timeit.timeit('seq_sum(640)', number=100, globals=globals()))     # 0.01576737499999581
print(timeit.timeit('seq_sum(1280)', number=100, globals=globals()))    # 0.04553108000254724
print(timeit.timeit('seq_sum(2560)', number=100, globals=globals()))    # 0.06476698500046041
print(timeit.timeit('seq_sum(5120)', number=100, globals=globals()))    # 0.12945073200171464

cProfile.run('seq_sum(100_000)')
#       4 function calls in 0.026 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.025    0.025 <string>:1(<module>)
#      1    0.025    0.025    0.025    0.025 task_1_1.py:37(seq_sum)
#      1    0.000    0.000    0.026    0.026 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

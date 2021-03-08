import timeit
import cProfile


# 3. По замерам for оказался быстрее, попробуем массив внутри for и sum()
def seq_sum(n):
    return sum([1 / -2**i if i % 2 else 1 / 2**i for i in range(n)])


print(timeit.timeit('seq_sum(10)', number=100, globals=globals()))      # 0.0005988619996060152
print(timeit.timeit('seq_sum(20)', number=100, globals=globals()))      # 0.0009793030003493186
print(timeit.timeit('seq_sum(40)', number=100, globals=globals()))      # 0.0027168790002178866
print(timeit.timeit('seq_sum(80)', number=100, globals=globals()))      # 0.010418131001642905
print(timeit.timeit('seq_sum(160)', number=100, globals=globals()))     # 0.021878543997445377
print(timeit.timeit('seq_sum(320)', number=100, globals=globals()))     # 0.0366774690010061
print(timeit.timeit('seq_sum(640)', number=100, globals=globals()))     # 0.0727364669983217
print(timeit.timeit('seq_sum(1280)', number=100, globals=globals()))    # 0.15847162600039155
print(timeit.timeit('seq_sum(2560)', number=100, globals=globals()))    # 0.3788265520015557
print(timeit.timeit('seq_sum(5120)', number=100, globals=globals()))    # 1.2899324579993845

cProfile.run('seq_sum(100_000)')
#       6 function calls in 8.498 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    8.498    8.498 <string>:1(<module>)
#      1    0.002    0.002    8.498    8.498 task_1_3.py:6(seq_sum)
#      1    8.494    8.494    8.494    8.494 task_1_3.py:7(<listcomp>)
#      1    0.000    0.000    8.498    8.498 {built-in method builtins.exec}
#      1    0.001    0.001    0.001    0.001 {built-in method builtins.sum}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""
Выводы:
    Самым быстрым оказался вариант с циклом for (task_1_1) O(n),
    немного медленнее второй - с циклом while (task_1_2) O(n).
    Ну и генератор списков просто поразил своей медленностью (task_1_3), O(2n),
    {сначала генератор - это 1 цикл, затем сумма - снова пробегается по полученному массиву}
    причём по cProfile очевидно, что проблема именно в генераторе списка,
    видать слишком много вычислений делаю внутри.
Графики:
    https://docs.google.com/spreadsheets/d/15TCdPzjQWugJZZj1KhmmNSsYZoGLtNkFhgsYWdSSxOk/edit?usp=sharing
"""
import timeit
import cProfile


# 2. Интересно, кто быстрее while или for
def seq_sum(n):
    spam = 1
    sum_ = 0

    i = 1
    while i <= n:
        sum_ += spam
        spam = spam * -0.5
        i += 1

    return sum_


print(timeit.timeit('seq_sum(10)', number=100, globals=globals()))      # 0.0002773870000964962
print(timeit.timeit('seq_sum(20)', number=100, globals=globals()))      # 0.0005707029995392077
print(timeit.timeit('seq_sum(40)', number=100, globals=globals()))      # 0.0012428340014594141
print(timeit.timeit('seq_sum(80)', number=100, globals=globals()))      # 0.002166777998354519
print(timeit.timeit('seq_sum(160)', number=100, globals=globals()))     # 0.004194599998299964
print(timeit.timeit('seq_sum(320)', number=100, globals=globals()))     # 0.01147652099825791
print(timeit.timeit('seq_sum(640)', number=100, globals=globals()))     # 0.029617846001201542
print(timeit.timeit('seq_sum(1280)', number=100, globals=globals()))    # 0.03895317899878137
print(timeit.timeit('seq_sum(2560)', number=100, globals=globals()))    # 0.07288528699791641
print(timeit.timeit('seq_sum(5120)', number=100, globals=globals()))    # 0.1783875370019814

cProfile.run('seq_sum(100_000)')
#          4 function calls in 0.028 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.028    0.028 <string>:1(<module>)
#         1    0.028    0.028    0.028    0.028 task_1_2.py:6(seq_sum)
#         1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

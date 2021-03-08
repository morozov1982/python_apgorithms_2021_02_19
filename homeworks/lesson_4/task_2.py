"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».

    Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
    Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».

    Примечание. Вспомните классический способ проверки числа на простоту.

Пример работы программ:
    sieve(2)
    3
    prime(4)
    7
    sieve(5)
    11
    prime(1)
    2
"""
# Несмотря на возможность не сдавать вторую задачу, принял стратегическое решение решить её ;-)
import timeit
import cProfile


# 1. Без решета (n - порядковый номер простого числа)
def prime(n):
    if n == 0:
        return None
    primes = [2]  # всё равно начинается с 2-ки
    primes_len = 1  # избавился таким образом от len(), скорость повысилась
    span = 2
    while primes_len < n:
        span += 1
        for i in primes:
            if span == primes[-1] or span % i == 0:
                break
            else:
                primes.append(span)
                primes_len += 1
    return primes[-1]


print(timeit.timeit('prime(2)', number=100, globals=globals()))     # 0.00011211399942112621
print(timeit.timeit('prime(4)', number=100, globals=globals()))     # 0.00032733599982748274
print(timeit.timeit('prime(8)', number=100, globals=globals()))     # 0.000765266999223968
print(timeit.timeit('prime(16)', number=100, globals=globals()))    # 0.0018105149993061787
print(timeit.timeit('prime(32)', number=100, globals=globals()))    # 0.003502982999634696
print(timeit.timeit('prime(64)', number=100, globals=globals()))    # 0.0076885750004294096
print(timeit.timeit('prime(128)', number=100, globals=globals()))   # 0.017269757998292334
print(timeit.timeit('prime(256)', number=100, globals=globals()))   # 0.03743121399929805
print(timeit.timeit('prime(512)', number=100, globals=globals()))   # 0.06278299299992796
print(timeit.timeit('prime(1024)', number=100, globals=globals()))  # 0.12334370299868169

cProfile.run('prime(2048)')
#       2051 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      1    0.003    0.003    0.003    0.003 task_2.py:30(prime)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#   2047    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# просто разделитель
print('*' * 50)
print('*' * 50 + '\n')


# 2. С решетом Эратосфена
def sieve(num):
    # сделаем грубое допущение, что num-е простое число входит в диапазон от 0 до num * 10
    # (проверять будем на числах входящих в диапазон),
    # хотя умножение тоже съедает ресурс, не нашёл более умного варианта
    n = num * 10
    a = [0] * n
    for i in range(n):
        a[i] = i

    a[1] = 0

    m = 2
    while m < n:
        if a[m]:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    return b[num - 1]


print(timeit.timeit('sieve(2)', number=100, globals=globals()))     # 0.0040393990002485225
print(timeit.timeit('sieve(4)', number=100, globals=globals()))     # 0.0043986370001221076
print(timeit.timeit('sieve(8)', number=100, globals=globals()))     # 0.008223488001021906
print(timeit.timeit('sieve(16)', number=100, globals=globals()))    # 0.03037208599926089
print(timeit.timeit('sieve(32)', number=100, globals=globals()))    # 0.034097429999746964
print(timeit.timeit('sieve(64)', number=100, globals=globals()))    # 0.06383878199994797
print(timeit.timeit('sieve(128)', number=100, globals=globals()))   # 0.12926950400105852
print(timeit.timeit('sieve(256)', number=100, globals=globals()))   # 0.24082390399962605
print(timeit.timeit('sieve(512)', number=100, globals=globals()))   # 0.5083907250009361
print(timeit.timeit('sieve(1024)', number=100, globals=globals()))  # 1.0110327649999817

cProfile.run('sieve(2048)')
#          2316 function calls in 0.021 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#         1    0.021    0.021    0.021    0.021 task_2.py:53(sieve)
#         1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#      2312    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0


"""
Выводы:
    Лучше получился вариант без решета Эратосфена быстрее (O(n^2)) - 1-й вариант.
    Думаю проблема 2-го варианта скорее всего в том как я применяю решето
    (по меньшей мере O(n^2)
    {вначале увеличиваю т в 10 раз, а дальше 4 цикла, 2 из которых вложенные},
    наверняка есть менее затратный способ ;-)
Графики:
    https://docs.google.com/spreadsheets/d/15TCdPzjQWugJZZj1KhmmNSsYZoGLtNkFhgsYWdSSxOk/edit?usp=sharing
"""

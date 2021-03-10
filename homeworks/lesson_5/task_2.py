"""
2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.

    Например, пользователь ввёл A2 и C4F.

Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque

NUMS = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'])
N_SYS = 16


def sum_(n1, n2):
    n1 = n1.copy()
    n2 = n2.copy()
    res = deque()
    spam = 0  # в уме

    len1 = len(n1)
    len2 = len(n2)
    if len1 < len2:
        n1, n2 = n2, n1
        len1, len2 = len2, len1

    for i in range(len1):
        eggs = NUMS.index(n1.pop()) + spam  # сумма элементов
        if n2:
            eggs += NUMS.index(n2.pop())
        spam = eggs // N_SYS
        res.appendleft(NUMS[eggs % N_SYS])

    if spam:
        res.appendleft(NUMS[spam])

    return res


def mul_(n1, n2):
    res = deque()
    len1 = len(n1)
    len2 = len(n2)

    if len1 < len2:
        n1, n2 = n2, n1
        len1, len2 = len2, len1

    megaspam = deque()

    for i in range(len2):
        if i:
            zeroes = '0' * i
            megaspam = deque(zeroes)
        spam = 0
        m2 = NUMS.index(n2.pop())
        n1_copy = n1.copy()

        for j in range(len1):
            m1 = NUMS.index(n1_copy.pop())
            eggs = m1 * m2 + spam
            spam = eggs // N_SYS
            megaspam.appendleft(NUMS[eggs % N_SYS])

        if spam:
            megaspam.appendleft(NUMS[spam])
        if len(res):
            res_copy = res.copy()
            megaspam_copy = megaspam.copy()
            res = sum_(res_copy, megaspam_copy)
        else:
            res = megaspam.copy()
        megaspam.clear()

    return res


inp1 = input('Введи положительное целое шестнадцатеричное число\n>>> ')
inp2 = input('Введи ещё одно\n>>> ')

num1 = deque(inp1.upper())
num2 = deque(inp2.upper())

print('*' * 25)
print(f'Сумма: {sum_(num1, num2)}')
print(f'Произведение: {mul_(num1, num2)}')

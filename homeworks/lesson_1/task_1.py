"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

number = int(input('Введи трёхзначное число: '))

a = number // 100
b = (number // 10) % 10
c = number % 10

summary = a + b + c
multiply = a * b * c

print(f'Сумма чисел: {a} + {b} + {c} = {summary}')
print(f'Произведение чисел: {a} * {b} * {c} = {multiply}')

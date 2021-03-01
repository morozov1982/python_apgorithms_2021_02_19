"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def digit_sum(n):
    if n == 0:
        return n
    return n % 10 + digit_sum(n // 10)


biggest_num = 0
biggest_sum = 0

while True:
    num = int(input('Введи натуральное число (для выхода - 0): '))

    if num == 0:
        break

    cur_sum = digit_sum(num)

    # не стал вводить проверку, если сумма цифр в числах окажется одинаковой
    if cur_sum > biggest_sum:
        biggest_sum = cur_sum
        biggest_num = num

print(f'Самое большое по сумме цифр из введённых - число: {biggest_num}\nСумма его чисел: {biggest_sum}')

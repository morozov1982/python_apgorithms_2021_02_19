"""
Схемы: https://drive.google.com/file/d/1fdFVJcvcZ6jTgvDm25iTPKP2Ae_RW_9Q/view?usp=sharing

3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


num = int(input('Введи натуральное число: '))

tmp = ""
while num > 0:
    tmp += f'{num % 10}'
    num //= 10

rev_num = int(tmp)

print(f'Введённое число задом наперёд: {rev_num}  # без нулей вначале')


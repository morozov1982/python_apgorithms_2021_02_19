"""
5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

letter_1 = input('Введи первую букву (от a до z): ')
letter_2 = input('Введи вторую букву (от a до z): ')

a_position = ord('a')
position_1 = ord(letter_1) - a_position + 1
position_2 = ord(letter_2) - a_position + 1

print(f'Позиция буквы "{letter_1}" в алфавите - {position_1}')
print(f'Позиция буквы "{letter_2}" в алфавите - {position_2}')

if position_1 == position_2:
    print('Введены одинаковые буквы')
else:
    letters_between = abs(position_1 - position_2) - 1
    print(f'Количество букв между ними: {letters_between}.')



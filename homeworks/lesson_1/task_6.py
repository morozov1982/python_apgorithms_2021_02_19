"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

letter_number = int(input('Введи номер буквы в алфавите (от 1 до 26): '))

a_position = ord('a')
letter = chr(letter_number + a_position - 1)

print(f'В английском алфавите {letter_number} буква - это "{letter}"')

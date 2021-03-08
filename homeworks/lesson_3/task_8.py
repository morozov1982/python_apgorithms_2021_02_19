"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
# 1 2 3   6
# 4 5 6   15
# 7 8 9   24
# 1 5 9   15
# 3 5 7   15


SIZE_R = 5
SIZE_C = 4
matrix = [[0 for _ in range(SIZE_C)] for _ in range(SIZE_R)]
print(*matrix, sep='\n')

for row in range(len(matrix)):
    row_sum = 0
    print(f'--- Строка {row + 1} ---')  # намеренно сделал нумерацию с 1
    for col in range(len(matrix[0]) - 1):
        user_num = int(input(f'Введи {col + 1} натуральное число (от 0 до 100): '))
        matrix[row][col] = user_num
        row_sum += user_num
    matrix[row][len(matrix[0]) - 1] = row_sum

for row in matrix:
    for idx, num in enumerate(row):
        print(f'{num:>5}', end='') if idx < (len(row) - 1) else print(f'\033[92m\033[1m{num:>7}\033[0;0m')

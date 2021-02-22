"""
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""


a = 5
b = 6

op_and = a & b
op_or = a | b
op_xor = a ^ b

op_right = a >> 2
op_left = a << 2

print(f'{a} & {b} = {op_and} или {bin(a)} & {bin(b)} = {bin(op_and)}')
print(f'{a} | {b} = {op_or} или {bin(a)} | {bin(b)} = {bin(op_or)}')
print(f'{a} ^ {b} = {op_xor} или {bin(a)} ^ {bin(b)} = {bin(op_xor)}')

print(f'{a} >> 2 = {op_right} или {bin(a)} >> 2 = {bin(op_right)}')
print(f'{a} << 2 = {op_left} или {bin(a)} << 2 = {bin(op_left)}')

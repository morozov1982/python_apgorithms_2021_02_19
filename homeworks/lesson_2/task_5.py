"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


first = 32
last = 127
count = 1
text = ''

for i in range(first, last + 1):
    text = text + f'{i}'.rjust(3, ' ') + f' - {chr(i)}'

    if count % 10:
        text = text + '   '
    else:
        text = text + '\n'

    count = count + 1

print(text)

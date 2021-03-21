"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.

Примечание: в сумму не включаем пустую строку и строку целиком.

Пример работы функции:
func("papa")
6
func("sova")
9
"""
import hashlib


def func(s: str) -> int:
    sub_set = set()
    len_ = len(s)

    for i in range(len_):
        for j in range(i, len_ - 1 if i == 0 else len_):
            sub_set.add(hashlib.sha1(s[i:j+1].encode('utf-8')).hexdigest())

    return len(sub_set)


str1 = 'papa'
print(f'\n\33[92mВ строке\33[0m "{str1}" \33[92m{func(str1)} подстрок\33[0m')

str2 = 'sova'
print(f'\n\33[92mВ строке\33[0m "{str2}" \33[92m{func(str2)} подстрок\33[0m')

str3 = 'Спасибо за отличный курс, веселье, музыку, видео и др. ;-)'

print(f'\nВ строке \33[93m"{str3}"\33[0m {func(str3)} подстрок')

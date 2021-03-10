"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import Counter

PERIODS = 4
firms_data = []
avgs = Counter()
avg = 0
profitable = []
unprofitable = []

num = int(input('Введи количество предприятий (более 1)\n>>> '))
print('*' * 50)  # понапихал их для красоты

for f in range(num):
    firm = {}
    name = input(f'Название предприятия № {f + 1}: ')
    firm['name'] = name
    total_profit = 0

    for p in range(1, PERIODS + 1):
        profit = int(input(f'Прибыль за {p} квартал: '))
        total_profit += profit
        firm[f'q{p}'] = profit

    avgs[name] = total_profit / PERIODS
    firm['avg'] = avgs[name]
    firms_data.append(firm)

    print('*' * 50)

print('*' * 50)

avg = sum(avgs.values()) / len(avgs)
print(f'Средний доход = {avg}\n')

for firm in firms_data:
    profitable.append(firm['name']) if firm['avg'] >= avg else unprofitable.append(firm['name'])

print(f'Прибыль выше среднего (или равна) у: {", ".join(profitable)}')
print('*' * 50)
print(f'Прибыль ниже среднего у: {", ".join(unprofitable)}')

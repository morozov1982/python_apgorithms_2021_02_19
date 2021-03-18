# Важные заметки по 7 уроку (лично для меня)

**12:10** - Разбор д/з


## Тема урока №7: *"Алгоритмы сортировки"* (41:45)

Практически каждый **алгоритм сортировки** можно разбить на **3 части**:
1. **Сравнение**, определяющее упорядоченность пары элементов;  
2. **Перестановка**, меняющая местами пару элементов;  
3. Сортирующий **алгоритм**, который сравнивает и переставляет элементы<br />
   до тех пор, пока все они не будут упорядочены.

**46:20** - Набор данных для тренировки (task_1.py):
``` Python3
import random

array = [i for i in range(10)]
print(array)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

random.shuffle(array)
print(array)  # [4, 5, 9, 6, 3, 2, 7, 8, 0, 1]
```


### Сортировка "пузырьком" (49:00)

``` Python3
# task_2.py
array = [4, 5, 9, 6, 3, 2, 7, 8, 0, 1]

n = 1
while n < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    n += 1
    print(array)

print(array)
```


### Сортировка выбором (54:50)

``` Python3
# task_3.py
def selection_sort(data):
    for i in range(len(data)):
        spam = i
        for j in range(i + 1, len(data)):
            if data[j] < data[spam]:
                spam = j
        data[spam], data[i] = data[i], data[spam]
        print(data)

array = [4, 5, 9, 6, 3, 2, 7, 8, 0, 1]
selection_sort(array)
print(array)
```


### Сортировка вставками (01:04:30)

``` Python3
# task_4.py
def insertion_sort(data):
    for i in range(1, len(data)):
        spam = data[i]
        j = i
        while data[j - 1] > spam and j > 0:
            data[j] = data[j - 1]
            j -= 1
        data[j] = spam
        print(data)

array = [4, 5, 9, 6, 3, 2, 7, 8, 0, 1]
insertion_sort(array)
print(array)
```

**01:11:30** - Слайд с быстрой сортировкой + видео:<br />
[Quick-sort with Hungarian (Küküllőmenti legényes) folk dance](https://youtu.be/ywWBy6J5gz8)


### Быстрая сортировка (01:23:30)

``` Python3
# task_5.py
import random

def quick_sort(data, first, last):
    print(data[first:last+1])
    if first >= last:
        return

    pivot = data[random.randint(first, last)]
    i = first
    j = last
    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i, j = i + 1, j - 1

    quick_sort(data, first, j)
    quick_sort(data, i, last)

array = [4, 5, 9, 6, 3, 2, 7, 8, 0, 1]
quick_sort(array, 0, len(array) - 1)
print(array)
```


### Сортировка Шелла (01:36:30)

``` Python3
# task_6.py
def shell_sort(data):
    assert len(data) < 4_000, 'Попробуй другую сортировку :-)'

    def new_inc(data):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]  # из матем. справочника
        while len(data) <= inc[-1]:  # если массив меньше
            inc.pop()  # удаляем значение (с конца)
        while inc:
            yield inc.pop()

    for cur_inc in new_inc(data):
        for i in range(cur_inc, len(data)):
            for j in range(i, cur_inc - 1, -cur_inc):
                if data[j - cur_inc] <= data[j]:
                    break
                data[j], data[j - cur_inc] = data[j - cur_inc], data[j]
            print(data)

array = [4, 5, 9, 6, 3, 2, 7, 8, 0, 1]
shell_sort(array)
print(array)
```

**01:51:50** - *Есть ли вопросы?*


### Сортировка сложных структур с использованием ключа (01:52:35)

``` Python3
# task_7.py
from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', 'age, name')

people = [
    Person(42, 'Arkady'),
    Person(78, 'Medok'),
    Person(45, 'Trump'),
    Person(75, 'Trump'),
    Person(45, 'Alex'),
    Person(12, 'Arkady'),
    Person(8, 'Tom'),
]

res = sorted(people, key=attrgetter('name'))  # только по имени
print(res)
# если возраст совпадает, сортировка по имени сохраняется от предыдущей
new_res = sorted(res, key=attrgetter('age'))
print(new_res)
```

**02:09:00** - *Вопросы*


## Как выполнять д/з (02:10:55)

**02:11:30** - **1-я задача**

Сортировка по убыванию методом "пузырька", важно:
1. По убыванию;
2. Целочисленный (int) массив;
3. Диапазон [-100; 100): от -100 (включительно), до 100 (исключая 100).

***Что нужно сделать:***

1. Взять пример из урока и обернуть его в функцию (без return):
``` Python3
size = 10  # удобный размер массива

def bubble_sort(data):
    pass
```

2. Улучшить "пузырёк", сделать алгоритм сортировки быстрее + умнее:
    + не испортить превращением в "расчёску", шейкер или др. алгоритм;
    + можно почитать в [википедии](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%BF%D1%83%D0%B7%D1%8B%D1%80%D1%8C%D0%BA%D0%BE%D0%BC).

**02:15:00** - **2-я задача**

Сортировка по возрастанию методом слияния, важно:
1. Вещественный (float) массив;
2. Диапазон [0; 50): от 0 (включительно), до 50 (исключая 50).

***Что нужно сделать:***

Открыть [Википедию](https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC), прочитать текстовое описание алгоритма слияния.<br />
   **Не брать** код для Python оттуда, он кривой:
``` Python3
def merge_sort(data):
    pass
```

**02:17:45** - **3-я задача**

Использовать сортировку, которой не было на уроке (например гномья).
``` Python3
m = 10
size = 2 * m + 1  # нечётное число элементов

def gnome_sort(data):
    pass
```

В массиве `[4, 5, 1, 8, 2]` медианой (средний элемент) будет `4`<br />
в отсортированном массиве она посередине `[1, 2, 4, 5, 8]`.

В массиве `[4, 4, 1, 4, 2]` - `4` (любая) - `[1, 2, 4, 4, 4]`

"не больше" - <=<br />
"не меньше" - >=

**02:23:00** - *Вопросы*

**02:26:15** - спойлер про алгоритм сортировки "слияние":<br />
[Merge-sort with Transylvanian-saxon (German) folk dance](https://youtu.be/XaqR3G_NVoo)
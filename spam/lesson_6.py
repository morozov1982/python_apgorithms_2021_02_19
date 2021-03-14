import sys

a = 100
b = 123 - 23
c = 1000
d = 1234 - 234
print(id(a), id(b), id(c), id(d))  # 9788064 9788064 140421504879504 140421504879504


e = 'Hello world!'
f = e
g = 'Hello world!'
del f
print(sys.getrefcount(e))


print(sys.getrefcount(True))   # 109
print(sys.getrefcount(False))  # 113
print(sys.getrefcount(None))   # 4088

print('*' * 50)
i = 42654562435536436263445453474537685638356737543256257543724
print(sys.getsizeof(i//1))
print(i//1)
f = 45736346752.54657435678625634
print(sys.getsizeof(f))
print(f)
print(sys.getsizeof('Hello world!ж'))

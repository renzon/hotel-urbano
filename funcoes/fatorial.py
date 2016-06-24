def fatorial(n):
    'retorn !n'
    return 1 if n <= 1 else n * fatorial(n - 1)


fat = fatorial

print(fat(5))
print(dir(fat))
fat.bar = 'bar'
print(fat.__dict__)
print(fat.__name__)
fat.__name__ = 'Foo'
print(fatorial.__name__)
print(dir(fat.__code__))
print(fat.__code__.co_varnames)
print(fat.__code__.co_code)

from dis import dis

print(dis(fat.__code__.co_code))

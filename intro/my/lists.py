fruits = "caqui banana abacaxi morango pequi".split()

def inverted(word):
    return word[::-1]

print(sorted(fruits))
print(sorted(fruits, key=len))
print(sorted(fruits, key=inverted))

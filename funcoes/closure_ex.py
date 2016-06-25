def acumulador_construtor():
    total = 0

    def acumular(n):
        nonlocal total
        total += n
        return total

    return acumular


acumulador1 = acumulador_construtor()
print(acumulador1(1))
print(acumulador1(4))
print(acumulador1(5))
acumulador2 = acumulador_construtor()
print(acumulador2(2))
print(acumulador2(2))
print(acumulador2(2))

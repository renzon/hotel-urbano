def logadora(funcao):
    def funcao_com_log():
        print('Execuntado funcao %s' % funcao.__name__)
        return funcao()

    return funcao_com_log


def f():
    return 'Executando F'

@logadora
def g():
    return 'Executando G'


print(f)
f = logadora(f)
print(f)
# g = logadora(g)

print(f())
print(f())
print(g())
print(g())

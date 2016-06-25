class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vetor({x},{y})'.format(**self.__dict__)

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)

    def __mul__(self, escalar):
        return Vetor(self.x*escalar, self.y*escalar)


v = Vetor(1, 2)
v2 = Vetor(2, 2)
print(v)
print(v + v2)
print(v*2)
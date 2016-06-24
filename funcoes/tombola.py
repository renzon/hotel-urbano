from random import shuffle


class Tombola():
    def __init__(self, bolas):
        self.bolas = bolas
        self.embaralhar()

    def embaralhar(self):
        shuffle(self.bolas)

    def sortear(self):
        return self.bolas.pop()

    def __call__(self):
        return self.sortear()



if __name__ == '__main__':
    t = Tombola(list(range(5)))
    print(t())
    print(t())
    print(t())
    print(t())
    print(t())

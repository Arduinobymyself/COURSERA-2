class Racional:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "%d/%d"%(self.num, self.den)

# testes
a = Racional(2, 3)
print(a)
b = Racional(1, 4)
print(b)


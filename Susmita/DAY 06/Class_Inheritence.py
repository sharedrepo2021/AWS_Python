class Animal:
    def __init__(self, legs, eyes, mouth, tail):
        self.legs = legs
        self.eyes = eyes
        self.mouth = mouth
        self.tail = tail

    def printname(self):
        print(self.legs, self.eyes, self.mouth, self.tail)

class Fish(Animal):
    def __init__(self, eyes, mouth, tail, fins):
        super().__init__(self, eyes, mouth, tail)
        self.fins = fins

    def printfish(self):
        print(self.fins)


a = Animal(4, 2, 1, 1)
a.printname()
f = Fish(2, 1, 1, 4)
f.printname()
f.printfish()
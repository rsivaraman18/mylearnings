#()
class Parent:
    i=100
    def __init__(self):
        self.j = 200
        print('hiii super class constructor')

    def test(self):
        self.k=500
        print('Testing super class')

class child(Parent):
    def __init__(self):
        super().__init__()
        super().test()

    def metre(self):
        #print(super().i)
        print(self.j)
        print(self.k)

obj = child()
obj.metre()

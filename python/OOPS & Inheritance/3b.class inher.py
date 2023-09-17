class humanbeing():
    total = 100000
    
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        self.time = 7

    def read(self):
        self.book='pyyhon'
        print('I read everyday')

class Employee(humanbeing):
    def __init__(self,name,degree,salary):
        #super().__init__('ajay',50)
        self.name    = name
        self.degree  = degree
        self.salary  = salary

    def work(self):
        print('i have to work daily')

    def Emp_det(self):
        print(self.name)
        print(self.degree)
        print(self.salary)
        print(super().time)
        print(self.time)
        print(self.book)
        


emp1 = Employee('siva','BE',40000)
#emp1.work()
emp1.Emp_det()
print(emp1.age)



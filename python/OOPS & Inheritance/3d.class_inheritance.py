class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost

    def showroom(self):
        print('Vehicle Detailis ')
        print('The mileage Is ',self.mileage)
        print('The Cost is',self.cost)

#v=Vehicle('60kmph','1lakh')
#v.show()

class Car(Vehicle):
    def car_details(self):
        print('I am from Car')


c=Car(100,2000)
c.showroom()
c.car_details()



#()

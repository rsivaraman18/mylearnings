class Vehicle:
    
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost

    def showroom(self):
        print('****Vehicle Detailis *** ')
        print('The mileage Is ',self.mileage)
        print('The Cost is',self.cost)

class Car(Vehicle):
    
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres = tyres
        self.hp    = hp

    def car_details(self):
        print('*** Your Car details ***')
        print('No.of Tyres are:',self.tyres)
        print('The Horse Power is',self.hp)

key =Car(100,200,300,400)
key.car_details()
key.showroom()

#()

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
    '''
    def __init__(self,name,qual):
        self.name = name
        self.qual = qual
        print('Hii from Car ')
        '''
    
    def car_details(self):
        print(' Car details not available')


c=Car('siva','teamplayer')
#c.showroom()
c.car_details()
 

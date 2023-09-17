class parent:
    nest1 = 100
    
    def __init__(self):
        self.nest2 = 200
        print('I am from parent init')

    def big(self):
        print('I am retired')
        nest3 = 300

class child(parent):
    def kutty(self):
        print('hii from kutty')
        
        #print(super().nest1)
        #print(self.nest2)
        print(self.nest3)
        

key=child()
key.kutty()
 

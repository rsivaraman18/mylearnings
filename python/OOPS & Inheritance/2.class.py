class call:
    def __init__(self,*arg):
        #for i in range(0,1):
            self.name =arg[0]
            self.age  =arg[1]
            self.qual =arg[2]
            self.cont =arg[3]
            self.perct =arg[4]

    def detail(self):
        print('details of student:',self.name,self.age,self.qual,self.cont,self.perct)
          

d=call('siva',100,'BE',9600543141,95)
d.detail()
            
#()

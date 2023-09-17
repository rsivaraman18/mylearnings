#()

x=10
def myname(a,b=x):
    global a
    print('value of A is',a)  #30
    print('value of B is',b)    #10

x=20
myname(30)
    

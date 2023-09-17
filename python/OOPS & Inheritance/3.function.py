#()
x=1
def fun1():
    global x
    x=1.5
    print('fun1',x)

def fun2(y,z):
    tot =  x+y+z
    print('total is:',tot)


    
    
    
fun1()
fun2(3,4)

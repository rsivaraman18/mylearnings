a=100
def callme():
    global a
    a=200
    a=a+1
    
    print('The value of a inside:',a)

a=200  #global variable
print('The value outside1',a)
callme()
#a=1
print('the value outside2:',a)

x=100
def fun1():
    global x
    x=75
    print('fun1 X value:',x)

'''
def fun2():
    print('fun2 X value:',x)
'''
def fun3():
    x=25
    print('fun3 X value:',x)
    print(globals()['x'])

#fun1()

fun3()



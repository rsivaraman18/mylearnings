#()

x=5
def call():
    x=7
    global x
    x=4
    X=10
    print('value of x:',x)

call()

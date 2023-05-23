# ( )

'''

    *
    **
    ***
    ****
    *****
    ******
    *******

'''

def triangle1(n):
    print("using For Loop ")
    for row in range(1,n):
        for col in range(row):
            print('*',end='')
        print( )
    

def triangle2(n):
    row = 1
    while row<=n:
        for col in range(row):
            print('*',end='')
        print( )
        row = row + 1

      
def triangle3(n):
    i =1
    while i<=n:
         print('*'*i)
         i = i + 1


triangle1(10)
triangle2(10)
triangle3(10)        


























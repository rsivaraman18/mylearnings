# ( )

'''
        ******
        *****
        ****
        ***
        **
        *
'''

def triangle1(n):
    print("using For Loop ")
    for row in range(n,0,-1):
        for col in range(row):
            print('*',end='')
        print( )



def triangle2(n):
    i =1
    while(n>=1):
        print('*'*n)
        n = n-1



        
triangle1(10)
print( )
triangle2(7)























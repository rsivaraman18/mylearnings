# ( )

'''
        *
       **
      ***
     ****
    *****    
'''

def triangle1(n):
    for row in range(1,n):
        print(' '*(n-row) , '*'*row) #space given


def triangle2(n):
    for row in range(n,0,-1):
        for col in range(row):
            print(' ',end='')        # Space Given
        for col in range(n-row):
            print('*',end='' )
        print( )
  

def triangle3(n):
    i = 1
    while(n>=i):
        print(' '*(n-i) , '*'*i)    #space given      
        i = i +1
        
        

triangle1(7)
triangle2(7)
triangle3(7)


'''

def triangle2(n):
    for row in range(n,0,-1):
        for col in range(row):
            print(' ',end='')
        for col in range(n-row):
            print(' *',end='' )
        print( )
'''























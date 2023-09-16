def triangle1(n):
    print('INverted triangle')
    for row in range(1,n+1):
        #print(' '*(row-1) , ' *'*(n-row)) 
        print(' '*(row) , ' *'*(n-row+1))
         

 

def triangle(n):
    print('Triangle')
    for row in range(1,n+1):
        print(' '*(n-row+1), ' *'*(row))

triangle1(5)
triangle(5)

print('********')

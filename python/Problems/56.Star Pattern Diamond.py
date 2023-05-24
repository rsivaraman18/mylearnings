def diamond(n):
    print('Diamond Triangle')
    for row in range(1,n+1):
        print(' '*(n-row+1) , ' *'*(row))   # Extra space
    for row in range(1,n+1):
        print(' '*(row+1) , ' *'*(n-row))   # Extra space
        

diamond(7)


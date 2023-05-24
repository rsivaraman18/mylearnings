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
    for row in range(1,n):
        print(' '*(row-1),'*'*(n-row))

triangle1(10)


def triangle2(n):
    i= 0
    while n>=1:
        print(' '*i, '*'*n)
        n = n-1
        i = i+1

triangle2(7)

# ()

def square1(n):
    for row in range(1,n+1):
        for col in range(1,n+1):
            print(col,end='')
        print()
    print('*********************')   



def square2(n):
    for row in range(1,n+1):
        for col in range(1,n+1):
            print(row,end='')
        print()
    print('********************')   


def square3(n):
    for row in range(n,0,-1):
        for col in range(1,n+1):
            print(row,end='')
        print()
    print('********************')   






square1(5)       
square2(5)
square3(7)

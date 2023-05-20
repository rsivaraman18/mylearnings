print('program to print factorial of a given number')

def fact1( ):
    total = 1
    num = 1
    maximum = int(input("Enter the max value: " ))
    while (num <=maximum):
        total = total * num
        num = num + 1
    print('Factorial of ',maximum,'is',total)
    print('*'*40)
    

def fact2( ):
    low   = int(input("Enter the Lower value: " ))
    upper = int(input("Enter the Upper value: " ))
    for num in range(low,upper+1):
        i = 1
        fact = 1
        while(i<=num):
            fact = fact * i
            i = i + 1
        print('Factorial of given number',i-1,'is -->',fact)
    print('*'*40)



fact1( )
fact2( )

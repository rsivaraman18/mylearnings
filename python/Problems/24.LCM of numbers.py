
def divisor( ):
    print('LCM of two number')
    num1 = int(input('Enter 1st number : '))
    num2 = int(input('Enter 2nd number : '))
    #div = 2
    big = num2 if (num1 < num2) else num1
    
    while True:
        if(big % num1 ==0) & (big % num2 ==0):
            print('LCM OF NUMBER IS',big)
            break
        big = big + 1
    
    print("LCM of two number",num1,'&',num2," is",big)


divisor( )

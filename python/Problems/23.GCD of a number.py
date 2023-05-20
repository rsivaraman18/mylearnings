# ( )
# print( )
def divisor( ):
    
    num1 = int(input('Enter 1st number : '))
    num2 = int(input('Enter 2nd number : '))
    div = 2
    small = num2 if (num1 > num2) else num1
    print('Small Value',small)
    while (div<small):
        if(num2 % div ==0) & (num1 % div==0):
            print(div)
            gcd = div
        div = div + 1
    else:
        print("GCD of two number is",gcd)


divisor( )

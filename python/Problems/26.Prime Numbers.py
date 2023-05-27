print('Program To find Prime Number')
print('*'*55)

def prime1( ):
    print('Check Prime Number using For loop')
    num = int(input('Enter number : '))
    for div in range(2,num):
        if num%div ==0:
            print('Not Prime' )
            break
    else:
        print( 'Prime Number')

    print('*'*55)


#***********************************************************

def prime2():
    print('Check Prime Number using while loop')
    num = int(input('Enter any no to check for prime : '))
    div =2
    while(num>div):
        if (num%div ==0):
            print('It is not a prime')
            break
        else:
            div = div + 1    
    else:
        print('It is a prime')

    print('*'*55)



#**********************************************************


def prime3():
    print('Check Range of number is PM or not')
    upper = int(input('Enter Upper limit value : '))
    lower = int(input('Enter Lower limit value : '))
    for i in range(upper,lower):
        num = i
        div =2
        while(num>div):
            if (num%div ==0):
                #print(num,'is not a prime')
                break
            else:
                div = div + 1    
        else:
            print(num,'is a prime')
    print('*'*55)



#**********************************************************
def prime4():
    upper = int(input('Enter Upper limit value : '))
    lower = int(input('Enter Lower limit value : '))
    for num in range(upper,lower):
        if all( (num%i!=0) for i in range (2,num) ):
            print(num )
    print('*'*55)
            


#**********************************************************

prime1()
prime2()
prime3()
prime4()



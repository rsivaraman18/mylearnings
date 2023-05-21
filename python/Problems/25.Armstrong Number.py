
def Arm1( ):
    print('Armstrong  number')
    num = int(input('Enter any number : '))
    sum = 0
    temp = num
        
    
    while temp>0:
        d = temp% 10
        pow = d**3
        sum = sum + pow
        temp = temp//10
    if num == sum:
        print("Armstrong Number" )
    else:
        print("Not Armstrong Number" )
    print('*'*45 )
    


def Arm2( ):
    print('Armstrong  number range')
    upper = int(input('Enter upper limit number : '))
    lower = int(input('Enter lower limit number : '))

    for num in range(upper,lower):
        sum = 0
        temp = num
        while(temp > 0):
            d = temp% 10
            pow =d**3
            sum = sum + pow
            temp = temp//10
        if num == sum:
            print('Armstrong Numbers are',num )
    print('*'*45 )
        
    





Arm1( )
Arm2( )











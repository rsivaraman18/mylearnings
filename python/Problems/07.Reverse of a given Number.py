
def reverse():
    n = int(input("Enter any number to reverse : "))
    rev = 0
    while( n>0):
        dig=n%10
        
        
        rev=rev*10 + dig
        n=n//10
    print('REVERSE OF A NUMBER:',rev )

reverse()

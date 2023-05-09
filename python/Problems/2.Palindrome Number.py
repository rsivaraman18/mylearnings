''' Eg of Palindrome --> 121, 1331,12321 '''
n= int(input("Enter any number to check for Palindrome : "))

temp=n
rev=0
while(temp>0):
    dig=temp%10
    rev=rev*10 + dig
    temp=temp//10
if n==rev:

    print( 'palindromne')
else:
    print( 'not palindrome')

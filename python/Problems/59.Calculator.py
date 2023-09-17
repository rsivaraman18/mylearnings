title = "Basic Calculator"
# ()
print()
print(title.center(75,"*" )  )
repeat = "Y"
print( "Choice of Operation : \t + --> for Add \t - --> for Sub \t * --> for Multiply \t / --> for Quotient \t % --> for Remainder ") 

while repeat == "Y":
    
    n1,operator,n2 = input("Enter n1,operator,n2  --> Use space as separator: " ).split( )
    n1 = float(n1)
    operator =operator
    n2 =float(n2)

    if operator =="+":
        ans = n1+n2
        print()
        print(n1,'+',n2,'=',ans)
        print()
        
    if operator =="-":
        ans = n1-n2
        print()
        print(n1,'-',n2,'=',ans)
        print()

    if operator =="/":
        ans = n1/n2
        print()
        print(n1,'/',n2,'=',ans)
        print()

    if operator =="*":
        ans = n1*n2
        print()
        print(n1,'*',n2,'=',ans)
        print()

    if operator =="%":
        ans = n1%n2
        print()
        print(n1,'%',n2,'=',ans)
        print()

    else:
        y=input('Enter Y to continue or N to quit ')
        print('*'*75)
        print()
        repeat = y.upper()
        

    



















        


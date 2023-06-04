def sumofdigits():
    number = input("Enter any number : ")
    temp = str(number)
    total = 0
    for i in range(0,len(temp)):
        total = total + int(temp[i])
        
    print(total)

sumofdigits() 

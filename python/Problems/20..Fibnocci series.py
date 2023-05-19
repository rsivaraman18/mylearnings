print("Print Fibnocci Series Number")
number = int(input("Enter how many series of fibonacci required ? : "))

a=0
b=1

print(a)                  
while(number>0):
    res=a+b
    print(res)
    a=b
    b=res
    number=number-1

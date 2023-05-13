def add1(n1,n2):
    print("Add 2 numbers")
    add = n1+n2
    return add

n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the Second number : "))
print("Addition of Numbers is",add(n1,n2))

#**************************************************************************
def add2():
    print("Multiple Numbers can be added ")
    numbers  = input("Enter the numbers separated by comma  :")
    numbers  = list(map(int,numbers.split()))  # Converts to int & append number in List
    addition = sum(numbers)
    print(addition)

add2()

#********************************************************************************************
def add3(*numbers):
    addition=0
    for number in numbers:
        addition += number
    return addition

print("Addition of multiple numbers using function method" ,add3(10,20,30))



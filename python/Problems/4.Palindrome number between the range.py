'''This is used to check Palindrome Number between Given range'''
Lower = int(input("Enter the lower limit value : ")) 
Upper = int(input("Enter the Upper limit value : ")) 

box = [ ]
for num in range(Lower,Upper+1):
    temp = num
    rev_num = 0
    
    while(temp>0):
        dig=temp%10
        rev_num = rev_num*10 + dig
        temp=temp//10
        
    if num == rev_num:
        box.append(num)
print("Palindrome Numbers between ",Lower,'&',Upper,"are listed below",box)
    

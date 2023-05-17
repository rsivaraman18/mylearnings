# ()
print("Print aplhabets based on the number on right side")

def mtd1():
    word='a4b3c2z1'
    #req=aaaabbbccz
    result=''
    
    for let in word:
        if let.isalpha():
            text = let
        else:
            num = int(let)
            result = result+(text*num)
        
    print('Given String:',word)
    print('RequiredString:',result)
    print('*'*40)


mtd1()

def mtd2():
    word = input("Enter a alpha numeric word: ")
    result=''
    
    for let in word:
        if let.isalpha():
            text = let
        else:
            num = int(let)
            result = result+(text*num)
        
    print('Given String:',word)
    print('RequiredString:',result)
    print('*'*40)


mtd2()
    

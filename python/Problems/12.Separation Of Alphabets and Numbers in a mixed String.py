print("Separation Of Alphabets and Numbers in a mixed String")

def sep1():
       
    word='a444b4343c552z1'
    #req_word = abcz44443435521
    result=''
    text=[]
    num =[]
    for i in word:
        if i.isalpha():
            text.append(i)
        elif i.isnumeric():
            num.append(i)
            
    final=text+num    
    result=''.join(final)
        
    print('Given String:',word)
    print('Separation Of Letters and numbers:',result)
    print('*'*35)



sep1()


def sep2():
    word = input("Enter a mixed alpha numeric word: ")
    result=''
    text=[]
    num =[]
    for i in word:
        if i.isalpha():
            text.append(i)
        elif i.isnumeric():
            num.append(i)
            
    final=text+num    
    result=''.join(final)
        
    print('Given String:',word)
    print('Separation Of Letters and numbers:',result)
    print('*'*35)


sep2()



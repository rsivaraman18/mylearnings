print('Print Alphabet based on the integer')
'''
this method involves ASCII Value where a=97 & A=123
'''

def mtd1():
        
    word='a4k3b2'
    length=len(word)

    """
    #a=97
    #A=
    ()
    """
    i=0
    result=''
    while i<length:
        text=word[i]
        num =word[i+1]
        temp=chr(ord(text) +int(num))
        result = result +text +temp
        
        i=i+2

    print('Input Value:',word)  
    print('Expected Val:',result)
    print('*'*40)




def mtd2():
        
    word = input('Enter a alpha numeric word: ')
    length=len(word)

    """
    #a=97
    #A=
    ()
    """
    i=0
    result=''
    while i<length:
        text=word[i]
        num =word[i+1]
        temp=chr(ord(text) +int(num))
        result = result +text +temp
        
        i=i+2

    print('Input Value:',word)  
    print('Expected Val:',result)
    print('*'*40)



mtd1()
mtd2()




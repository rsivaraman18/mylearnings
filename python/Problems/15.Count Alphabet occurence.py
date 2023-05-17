# ()
print("Count alphabets occurence ")

def mtd1():
        
    word='aaaabbbccz' #4a3b2c1z
    length=len(word)
    old=word[0]
    output=''
    count=1
    i=1

    while i<length:
        if word[i] ==old:
            count=count + 1
        else:
            output=output+str(count)+old
            old=word[i]
            count=1
        if i==length-1:
            output=output+str(count)+old
            
        i=i+1
    print("Given string",word)
    print("Resuted String",output)
    print('*'*35)


def mtd2():
    word=input("Enter a Alpha string with repeated letters :")
    length=len(word)
    old=word[0]
    output=''
    count=1
    i=1

    while i<length:
        if word[i] ==old:
            count=count + 1
        else:
            output=output+str(count)+old
            old=word[i]
            count=1
        if i==length-1:
            output=output+str(count)+old
            
        i=i+1
    print("Given string",word)
    print("Resuted String",output)
    print('*'*35)



mtd1()
mtd2()

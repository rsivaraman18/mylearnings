print('Print a word after removing duplicates')
print('Example Tutorial')
print('Method 1: String Method')
print('Method 2: List Method')
print('*'*50)


def eg():
    word='sssivva11222'
    print('Given String is :',word)
    
    b=""
    for i in word:
        if i not in b:
            b = b+ i
    print('String Mtd duplicate Removed:',b)
    print('*'*50)

    



def mtd1():
    print('Using String Method')

    word=input('Enter a word:')
    print('Given String is :',word)
    
    b=""
    for i in word:
        if i not in b:
            b = b+ i
    print('String Mtd duplicate Removed:',b)
    print('*'*50)


def mtd2():
    print('Using List Method')

    mylist=[]
    for letter in word:
        if letter not in mylist:
            mylist.append(letter)

    result="".join(mylist)        

    print('Using list Mtd duplicate Removed:',result)
    print('*'*50)




eg()
mtd1()
mtd2()







    

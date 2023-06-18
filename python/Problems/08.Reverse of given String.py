s='computer programmer'

def mtd1():
    print("Using Slicing ")
    res=s[::-1]
    print('Given string:',s)
    print('Reversed string:',res)
    print('*'*25)


def mtd2():
    print("Without Using Slicing ")   
    name=''
    i=len(s)-1
    while(i>-1):
        name = name + s[i]
        i=i-1
    print('Given string:',s)
    print('Reversed string:',name)
    print('*'*25)


def mtd3():
    print("Using List Method")   
    s='My name is Siva'
    s1=s.split(' ')
    l1=[]

    for each in s1:
        l1.append(each[::-1])

    rev= ' '.join(l1)

    print('Given sentence:',s)    
    print('Sentence Reversed:',rev)
    print('*'*25)


def mtd4():
    n= 'Computer Programmer'
    print('Using For Loop --> Word or Number')
    temp = str(n)
    lnum = len(str(n))-1
    rev_num = ''
    for i in range(lnum,-1,-1):
        rev_num =rev_num + (temp[i])
    print('After Reversing',rev_num)
    print('*'*25)

mtd1()
mtd2()
mtd3()
mtd4()





def mtd1():
    str1='note'
    str2='bookss'
    s1=len(str1)
    s2=len(str2)
    i=0
    j=0


    result=''
    box1=[]

    while((i<s1)or (j<s2)):
        if (i<s1):        
            box1.append(str1[i])
            i=i+1
        if (j<s2):        
            box1.append(str2[j])
            j=j+1
        
        
    result=''.join(box1)
       
    print('Given String:',str1,str2)
    #print('box1:',box1)
    print('Result:',result)
    print('*'*30)


mtd1()

def mtd2():
    str1= input('Enter first word :')
    str2= input('Enter Second word :')
    s1=len(str1)
    s2=len(str2)
    i=0
    j=0


    result=''
    box1=[]

    while((i<s1)or (j<s2)):
        if (i<s1):        
            box1.append(str1[i])
            i=i+1
        if (j<s2):        
            box1.append(str2[j])
            j=j+1
        
        
    result=''.join(box1)
       
    print('Given String:',str1,str2)
    #print('box1:',box1)
    print('Result:',result)
    

mtd2()




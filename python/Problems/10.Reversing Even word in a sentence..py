s='One two three four five six seven eight'

s1=s.split(' ')
length=len(s1)
i=0
List1=[]

while(i<length):
    if(i%2==0):
        List1.append(s1[i])
    else:
        List1.append(s1[i][::-1])
    i=i+1

result=' '.join(List1)
    
print('Given sentence:',s)
print('result:',result)



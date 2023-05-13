str1='abcdefghijklmnopqrstuvwxyz'
s1=len(str1)

i=0

result=''
box1=[]
box2=[]
while(i<s1):
    if(i%2!=0):
        box1.append(str1[i])
    else:
        box2.append(str1[i])
    i=i+1

box1=''.join(box1)
box2=''.join(box2)
result =box1 +box2

   
print('Given String:',str1)
print('odd values:',box1)
print('even values :',box2)
print('Result:',result)

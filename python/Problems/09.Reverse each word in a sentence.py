s='One two three four five six seven eight'
'''req_op=eight seven six five four three two One'''

s1=s.split(' ')
length=len(s1)
i=1
List1=[]


while(i<=length):
    List1.append(s1[(length)-i])
    i=i+1
res=' '.join(List1)

print('Given Sent:',s)
print('Output:',res)

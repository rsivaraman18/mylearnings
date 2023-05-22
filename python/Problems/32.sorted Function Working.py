# ()
''' Sorted Fubnction '''
names = ['raman','kiwi','mangoes','apple','pomegranate','grapes' ]
print('Given: ',names)

'''Syntax --> sorted(Array,key=condition , reverse = True or false)'''

# Based On Alphabets Ascend
new = sorted(names)
print('Sort 1: ',new)

# Based On Alphabets Descend
new = sorted(names , reverse =True)
print('Sort 2: ',new)


# Based On length Ascend
new = sorted(names,key=len)
print('Sort 3: ',new)


# Based On length Descend
new = sorted(names,key=len , reverse =True)
print('Sort 4: ',new)

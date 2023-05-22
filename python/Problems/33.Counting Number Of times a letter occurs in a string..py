#  ( )

def countlet(word):
    
    d = { }
    for ch in word:
        d[ch] = d.get(ch,0) + 1
    for key , value in d.items():
        print('{} occurs : {} times'.format(key,value) )

    print('***'*10)
    
countlet('AABACADAS' )
countlet('Sivaraman' )


def countlet1(word):
    
    d = { }
    for ch in word:
        d[ch] = d.get(ch,0) + 1
    out = ''
    for key , value in d.items():
        out = out + str(value) + str(key)
    print(out)
     




countlet1('AABACADAS')
countlet1('AABACADAS')








    

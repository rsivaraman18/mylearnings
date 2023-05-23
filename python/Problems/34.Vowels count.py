#  ( )

def countlet(word):
    v = {'a','e','i','o','u','A','E','I','O','U'}   
    d = { }
    
    for ch in word:
        if ch in v:
            d[ch] = d.get(ch,0) + 1
            
    for key,value in d.items( ):
        print('{} occurs : {} times'.format(key,value))

    print('***'*10)
    
countlet('AABACADAS' )
countlet('Sivaraman' )

''' Sorting Technique 2 '''
# ()
def ASCsorting():
    given = [7,6,4,1,3,9,5,2,8,7,1,4]
    print ('Given List:',given)
    for i in range(0,len(given)):
        for j in range(i+1,len(given)):
            if given[i] >= given[j]:        # Only change here
                given[i],given[j]  = given[j],given[i]
    print('ascend sort',given)
    print('***'*20)
            
        
ASCsorting()    



def DSCsorting():
    given = [7,6,4,1,3,9,5,2,8,7,1,4]
    print ('Given List:',given)
    for i in range(0,len(given)):
        for j in range(i+1,len(given)):
            if given[i] <= given[j]:            # Only change here
                given[i],given[j]  = given[j],given[i]
    print('Descend sort',given)
    print('***'*20)
            
        
DSCsorting()    

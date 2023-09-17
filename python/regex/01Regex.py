'''
1.Search -To search  a item in a given statement.
2.It find the item in first instance only.It doesnot show if the same word occurs for multiple time.
( )
'''

'''
List of test cases
1.Find a word in the given sentence.
'''




def test1( ):
    Print("I Print The match")
    import re
    sent = "I love to swim in the morning"  
    x = re.search("swim", sent)
    print(x)
    #out -> <re.Match object; span=(10, 14), match='swim'>
    

def test2( ):
    print("I Print The match")
    import re
    sent = "I love swimming"  
    x = re.search("swim", sent)
    print(x)
    #out -> <re.Match object; span=(7, 11), match='swim'>
    

def test3( ):
    print("I print the match at first occurence only" )
    import re
    sent = "I love swimming.I practice swimming."  
    x = re.search("swim", sent)
    print(x)
    #out -> <re.Match object; span=(7, 11), match='swim'>


def test4( ):
    print("If no match,None will be printed" )
    import re
    sent = "I love swimming.I practice swimming."  
    x = re.search("siva", sent)
    print(x)
    #out -> None


def test5( ):
    print("case sensitive" )
    import re
    sent = "I love play"  
    x = re.search("i", sent)
    print(x)
    #out -> None



def test6( ):
    print("Search for white space" )
    import re
    sent = "Today is not interesting"  
    x = re.search("\s", sent)
    print(x)
    #out -> None



def test7( ):
    print("I can search a letter inside a word" )
    import re

    sent = "The rain in Spain"
    x = re.search("ai", sent)
    print(x) #this will print an object



#Search for an upper case "C" character in the beginning of a word, and print its position:
def test8( ): 
    import re
    sent = "The rain in Chennai"
    x = re.search(r"\ C\w+", sent)
    print(x)
    #out --> <re.Match object; span=(11, 19), match=' Chennai'>
    
   
#Search for an upper case "C" character in the beginning of a word.
def test9( ):
    import re
    sent = "The rain in Chennai"
    x = re.search(r"\ C\w+", sent)
    print(x.span())
    #out --> (11, 19)

   
#If word matches, Print the string passed into the function
def test10( ):
    import re
    txt = "The rain in Siva court"
    x = re.search(r"\bS\w+", txt)
    print(x.string)
    #out --> The rain in Siva court
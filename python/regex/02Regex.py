"""Findall"""

def test1( ):
    import re
    print("Find all occurence of word in a sentence" )
    sent = "The rain rain go away come again"
    x = re.findall("rain", sent)
    print(x)
    #out --> ['rain','rain']


def test2( ):
    import re
    sent = "The rain in Spain"
    x = re.findall("Sun", sent)
    print(x)
    #out --> []


def test3( ):
    import re
    txt =  "The rain in Spain Spain"
    x = re.search(r"\bS\w+", txt)
    print(x.group())

 
test3( )












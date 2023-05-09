'''This is used to check both word or number is a PALINDROME '''


word = input("Enter any word to check for Palindrome : ")
wordlen = len(word)

rev_word = ""
while(wordlen>0):
    letter   = word[wordlen -1]
    rev_word = rev_word + letter
    
    wordlen  = wordlen -1
    
print(rev_word)
if (word == rev_word):
    print("This is a Palindrome")
else:
    print("this is not a palindrome" )

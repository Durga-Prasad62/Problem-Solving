def longest_word(str1):
    word=""
    longest=""
    str1+=" "
    for i in str1:
        if i!=" ":
            word+=i
        else:
            if len(longest)<len(word):
                longest=word
            word=""
    print(longest)
longest_word("I Love Programming")
longest_word("Believe In Yourself Prasad")
longest_word("consistency is key to success")





           
        
        
    
            


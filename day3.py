# remove duplicates in str
# def  remove_duplicates(str1):
#     for ch in str1:
#      count=0
#      for freq in str1:
#         if ch==freq: 
#          count+=1
#      if count==1:
#       print(ch)
# remove_duplicates("madam")
# remove_duplicates("donkey")
# remove_duplicates("racecar")



# reverse vowel
def reverse_vowel(str1):
    rep=""
    for i in str1:
     if i in "aAEeIiOoUu":
        if i not in rep:
           rep+=i
    print(rep)   
reverse_vowel("Helloworld")
reverse_vowel("Jacksparrow")




# word=""
# for i in str1:
#     if'A'<=i<='Z':
#         res1= chr(ord(i)+32)
#         word=word+res1
#     elif 'a' <=i<='z':
#         res2=chr(ord(i)-32)
#         word=word+res2
# print(word)



def Conversion_Strings(str1):
    word=""
    for i in str1:
     if'A'<=i<='Z':
        res1= chr(ord(i)+32)
        word=word+res1
     elif 'a' <=i<='z':
        res2=chr(ord(i)-32)
        word=word+res2
    print(word)
Conversion_Strings("JohnWick")
Conversion_Strings("Korean")











   

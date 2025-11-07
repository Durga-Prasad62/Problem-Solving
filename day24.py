# str1="hello world"


def firstchar_last_char_cap(str1):
   str1+=" "
   for i in range(len(str1)):
      if i==0:#starting word capital
         if 'a'<= str1[i]<='z':
               print(chr(ord(str1[i])-32),end="")
         else:
               print(str1[i],end="")
      elif str1[i-1] == " ": #first character of next word
         if 'a' <= str1[i] <= 'z':
               print(chr(ord(str1[i]) - 32), end="")
         else:
               print(str1[i], end="")
   
      elif i < len(str1)-1 and str1[i+1]==" " : # last character of word
            if 'a'<=str1[i]<='z':
               print(chr(ord(str1[i])-32),end="")
            else:
               print(str1[i],end="")
      else:
         print(str1[i],end="")
   print()
firstchar_last_char_cap("hello world")
firstchar_last_char_cap("hello world python")
    







      

    




# str1="hello world"
# word=""
# str1+=" "
# for i in str1:
#     if i!=" ":
#         word+=i
#     else:
#        for j in range(len(word)):
#         if j==0:
#            if 'a'<=word[j]<='z':
#               print(chr(ord(word[j])-32),end=" ")
#               word=""
#            else:
#               print(word[j],end="")
    

            
          
                



# str1="hello world"
# for i in str1:
#     if i not in"aAEeIiOoUu":
#         print(i,end="")

# def removing_vowels(str1):
#      for i in str1:
#         if i not in"aAEeIiOoUu":
#             print (i,end="")
#      print()
# removing_vowels("hello world")
# removing_vowels("Jack Sparrow")


# str1="Jack Car sparrow"
# word=""
# for i in range(len(str1)):
#     if i==0:
#         if 'a'<=str1[i]<='z':
#          res=chr(ord(str1[i])-32)
#          print(res,end="")
#         else:
#            print(str1[i],end="")

#     elif str1[i-1]==" ":
#         if 'a'<=str1[i]<='z':
#          res=res=chr(ord(str1[i])-32)
#          print(res,end="")
#         else:
#            print(str1[i],end="")
  
#     else:
#         print(str1[i],end="")




def title(str1):
   for i in range(len(str1)):
        if i==0:
            if 'a'<=str1[i]<='z':
             res=chr(ord(str1[i])-32)
             print(res,end="")
            else:
             print(str1[i],end="")

        elif str1[i-1]==" ":
            if 'a'<=str1[i]<='z':
             res=res=chr(ord(str1[i])-32)
             print(res,end="")
            else:
             print(str1[i],end="")
    
        else:
            print(str1[i],end="")
   print()

    
title("hello world")
title("Hello world")
title("jack sparrow")
title("Jack sparrow")



   



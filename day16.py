# Print each word of sentence
def print_each_word(str1):
    word=""
    for i in str1:
        if i!=" ":
         word+=i
        else:
            print(word,end=" ")
            word=""
    if word:
        print(word,end=" ")
    print()
print_each_word("the sky is blue")
print_each_word("hello iam python")
print_each_word("Iam Learning Python")



















#Reverse of a String   
# def reverse_string(str1):
#     word=""
#     for i in range(len(str1)-1,-1,-1):
#         if str1[i]!=" ":
#             word+=str1[i]
#         else:
#             print(word[::-1],end=" ")
#             word=""
#     if word:
#         print(word[::-1],end=" ")
#     print()
# reverse_string("the sky is blue")
# reverse_string("I Love Python")
# reverse_string("I am  Learning  Python")

 #without slicing # using flag
# def reverse_string(str1):
#     word=""
#     result=""
#     first=True
#     for ch in str1:
#         if ch!=" ":
#             word+=ch
#         else:
#             if first:
#                 first=word 
#                 result=word +" "+ result
            
#                 first=False
#             else:
#                 result=word +" "+ result
            
#             word=""
#     if word:
#      result=word+" "+ result
#     print(result)
# reverse_string("the sky is blue")
# reverse_string("I Love Python")
# reverse_string("I am  Learning  Python")






n=5
i=1
num=1
while(i<=n):
    j=1
    while(j<=i):
        print(num,end=" ")
        num+=1
        j+=1
    print()
    i+=1




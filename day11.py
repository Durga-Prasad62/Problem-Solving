

# def string_palindrome(str1):
#     words=""
#     for i in str1:
#         words=i+words
#     if words==str1:
#         return True
#     else:
#         return(False)
# str1=input("enter a string:")
# print(string_palindrome(str1))
# print(string_palindrome("otto"))
# # with slicing
# def string_palindrome(str1):
#     words=""
#     for i in range(len(str1)):
#        words=str1[::-1]
        
#     if words==str1:
#         return True
#     else:
#         return(False)
# # str1=input("enter a string:")
# print(string_palindrome("malayalam"))
# print(string_palindrome("racecar"))


#count vowels in a str
def vowel_count(str1):
    count=0
    for i in str1:
        if i in "aAIiEeOoUu":
            count+=1
    print("Count of Vowels:",count)
vowel_count("Hello World")
vowel_count("Python")
vowel_count("Jack Sparrow")




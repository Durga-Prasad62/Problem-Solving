# #Swap first  and last character
# str1="Python"
# for i in  str1:
#    first,middle,last=str1[len(str1)-1],str1[1:-1],str1[0]
# print(first+middle+last)

#Swap first  and last character
def swap_first_last(str1):
#    for i in  str1:
    first,middle,last=str1[len(str1)-1],str1[1:-1],str1[0]
    print(first+middle+last)
swap_first_last("Hello")
swap_first_last("Python")
swap_first_last("World")

   
  
#  str1[0],str1[len(str1)-1]=str1[len(str1)-1],str1[0]
# In a string, the starting and ending (actually every character)
# are fixed once created  if we write this cause a error called
#TypeError: 'str' object does not support item assignment

#Add Underscore in the space of a string for example Hello World Python 
#output Hello_World_Python

# with Inbuilt Method
# def Add_Underscore(str1):
#     for i in str1:
#         if i==" ":
#             print(str1.replace(" ","_"))
#             break
# Add_Underscore("Hello World Python")
# Add_Underscore("I Love Programming")
# Add_Underscore("Have A Nice Day")
# #without using Inbuilt Method
# def Add_Underscore(str1):
#     underscore_str=""
#     for i in str1:
#         if i!=" ":
#             underscore_str+=i
#         else:
#              underscore_str+="_"
#     print(underscore_str)
# Add_Underscore("Hello World Python")
# Add_Underscore("I Love Programming")
# Add_Underscore("Have A Nice Day")



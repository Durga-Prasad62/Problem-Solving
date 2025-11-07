# s="123a4"
# prod=1
# for  i in s:
#  if  'a'<=i<='z 'or 'A'<=i<='Z' :
#    res=(ord(i)) 
#    while(res!=0):
#     rem=res%10
#     prod*=rem
#     res//=10
#  else:
#    prod*=int(i)
# print(prod)


     

# def product(s):
#     prod=1
#     for  i in s:
#      if  'a'<=i<='z'or 'A'<=i<='Z' :
#       res=(ord(i)) 
#       while(res!=0):
#         rem=res%10
#         prod*=rem
#         res//=10
#      else:
#       prod*=int(i)
#     print(prod)
# product("123a4")
# product("123b4")
# product("123C4")



# def product(s):
#   prod=1
#   for  i in s:
#    if  'a'<=i<='z'or 'A'<=i<='Z' :
#     for digit in str(ord(i)):
#       prod*=int(digit)
#    else:
#     prod*=int(i)
#   print(prod)
# product("123a4")
# product("123b4")
# product("123C4")





def remove_spaces(s):
  for i in s:
      if i==" ":
          continue
      else:
          print(i,end="")
  print()
remove_spaces("I am learning")
remove_spaces("I Love Python")
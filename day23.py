#banana b1a3n2

# str1=input("enter a string:")
# seen=set()
# for i in str1:
#     if i not in seen:
#       freq=i+str(str1.count(i))
#       print((freq),end="")
#       seen.add(i)





# def freq_char(str1):
#     seen=set()
#     for i in str1:
#         if i not in seen:
#           freq=i+str(str1.count(i))
#           print(freq,end=" ")
#           seen.add(i)
#     print()
# freq_char("banana")
# freq_char("apple")
# freq_char("orange")
# freq_char("python")
# freq_char("learning")













str1=input("enter a string:")
freq_dict={}
for i in str1:
    if i not in freq_dict:
      freq_dict[i]=str(str1.count(i))
print(freq_dict)

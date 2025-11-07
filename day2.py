
def first_last_middle_compare(num):
     first=num[0]
     last=num[-1]
     for i in range(1,len(num)-1):
       if not  (int(num[i])< int(first ) and int (num[i])< int(last)):
          print(False)
          break      
     else:
      print(True)
first_last_middle_compare("1672")
first_last_middle_compare("84719")




# def reverse_vowel(str1):
#     rev=""
#     for i in str1:
#      if i in "aAEeIiOoUu":
#         rev=i+rev
#     print(rev)
# reverse_vowel("Helloworld")
# reverse_vowel("JackspArrow")































        


     
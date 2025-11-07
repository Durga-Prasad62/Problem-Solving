#middle letters check
def middle_letters (str1):
    length=len(str1)
    if length%2==1:
      middle=length//2
      print(str1[middle])
    else:
         first_middle=length//2-1 
         second_middle=length//2
         print(str1[first_middle]+ str1[second_middle])
middle_letters("world")
middle_letters("wonder")
middle_letters("6969")
middle_letters("globe")
middle_letters("colorful")



#last+middle=sum
# def first_last_middle(num1):
#     first=0    #we can declare the first and last index  here its our wish  to reduce the code we need assaign before loop
#     last=0
#     middle_sum=0
#     length=len(num1)
#     for i in range(length):
#      if i==0:
#         first=num1[i]
#      elif i==len(num1)-1:
#         last=num1[i]
#      else:
#         middle_sum+=int(num1[i])
#     if int(first)+int(last)==middle_sum:
#      print("Equal")
#     else:
#      print("Not Equal")
# first_last_middle("75547")
# first_last_middle("765")
# first_last_middle("12345")
# first_last_middle("52535")
    
    

  










                   
      
         







    

        



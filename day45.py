#  Find the missing numbers. Input: 34571  	Output : 26 missing
num1 = 34751
# list1 =  list(num1)# int directly not  convert to list so we use list comphrension
list1 = [int(digit) for digit in str(num1)]
newlist=[]
list_min = min(list1)
list_max = max(list1)
for i in range(list_min,list_max+1):
    if i not  in list1:
        print(i)
    if i not  in newlist:
        newlist.append(i)
print(newlist)
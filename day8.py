# ascending sort
# def is_sorted_ascending(arr):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:  
#                 return False
#     return True

# list1=[1,2,3,4,5,6]
# list2=[1,3,6,7,8,2]
# list3=[4,5,6,7,8,9]
# print(is_sorted_ascending(list1))
# print(is_sorted_ascending(list2))
# print(is_sorted_ascending(list3))



# list1=[1, 2, 3, 4, 5]
# for i in range(len(list1)):
#    for j in range(i+1,len(list1)):
#       if list1[i]<list1[j]:
#          list1[i],list1[j]=list1[j],list1[i]
# print(list1)



#descending sort
def descending_sorted_list(arr):   
   for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i]<arr[j]:
         arr[i],arr[j]=arr[j],arr[i]
   print(arr)
list1=[1, 2, 3, 4, 5]
list2=[3,5,6,7,9,2]
list3=[6,7,8,3,9,3]
descending_sorted_list(list1)
descending_sorted_list(list2)
descending_sorted_list(list3)

                  

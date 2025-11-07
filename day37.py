# l=[1,2,3,4,5]
# i=0
# while True:
#     if i<len(l)-1 and l[i]<l[i+1]:
#         l[i],l[i+1]=l[i+1],l[i]
#         i+=1
#     else:
#         break      
# print(l)


# def Rotation(arr):
#     i=0
#     while True:
#         if i<len(arr)-1 and arr[i]<arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#             i+=1
#         else:
#             break 
#     return arr
# l=[5]
# l1=[1,2,3,4,5]
# l2=[5,4,3,2,1]
# print(Rotation(l))
# print(Rotation(l1))
# print(Rotation(l2))

# def Rotation_left(arr):
#     if len(arr)>0:
#        first= arr.pop(0)
#        arr.append(first)
#     return arr
# ls=[1,2,3,4,5]
# print(Rotation_left(ls))


# def Rotation_left(arr,k):
#         if len(arr)==0:
#             return arr
#         k=k%len(arr) 
#         return arr[k:]+arr[:k]
# ls=[1,2,3,4,5]
# print(Rotation_left(ls,2))
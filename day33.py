# Find the second minimum element in an array

# l=[1,3,4,5,6,74,2]
# max_val=float("-inf")
# smax_val=float("-inf")
# tmax_val=float("-inf")
# fmax_val=float("-inf")
# for i in range(len(l)):
#     if l[i]>max_val:
#         fmax_val=tmax_val
#         tmax_val=smax_val
#         smax_val=max_val
#         max_val=l[i]
#     elif l[i]>smax_val:
#         fmax_val=tmax_val
#         tmax_val=smax_val
#         smax_val=l[i]
#     elif  l[i]>tmax_val:
#          fmax_val=tmax_val
#          tmax_val=l[i]
#     elif l[i]<tmax_val and l[i]>fmax_val:
#         fmax_val=l[i]      
# print(fmax_val)        




l=[1,3,4,5,6,74,2]
min_val=sec_min_val=third_min_val=four_min_val=float('inf')
for i in range(len(l)):
    if l[i]<min_val:
        four_min_val=third_min_val
        third_min_val=sec_min_val
        sec_min_val=min_val
        min_val=l[i]
    elif l[i]<sec_min_val:
        four_min_val=third_min_val
        third_min_val=sec_min_val
        sec_min_val=l[i]
    elif  l[i]<third_min_val:
         four_min_val=third_min_val
         third_min_val=l[i]
    elif l[i]<four_min_val:
       four_min_val=l[i]      
print("firstminimum:",min_val)     
print("secondminimum:",sec_min_val) 
print("thirdminimum:",third_min_val)     
print("fourthminimum:",four_min_val)     



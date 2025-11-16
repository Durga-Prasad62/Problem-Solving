# ls = [10,20,30,40,50]
# k = int(input("enter steps"))
# if len(ls)<2:
#     print("not possible")
# k = k % len(ls)
# print(ls[k:]+ls[:k])

def ArrayRotation(arr,k):
    if len(arr)<2:
        return False
    k = k % len(arr)
    return arr[k:]+arr[:k]
print(ArrayRotation( [10,20,30,40,50],3))
    

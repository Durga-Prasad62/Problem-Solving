# 1. Check if a Matrix is Square
# Problem: Determine if the given matrix is square.
# Explanation: A matrix is square if the number of rows equals the number of columns.
# Input: [[1, 2], [3, 4]]
# Output: True

# rows,cols = map(int,input().split())
# matrix = []
# for i in range(rows):
#     row=list(map(int,input().split()))
#     matrix.append(row)
# if rows==cols:
#     print(True)
# else:
#     print(False)

# 2.First Half Reverse
# [1,2,3,4,5,6]---Input
# [3,2,1,4,5,6]---Output

def FirstHalfReverse (arr):
    low = 0
    high = (len(arr)-1)//2
    while(low<high):
        if arr[low]<arr[high]:
            arr[low],arr[high] = arr[high],arr[low]
            low+=1
            high-=1
    return arr
print(FirstHalfReverse([1,2,3,4,5,6]))
print(FirstHalfReverse(['a','b','c','d','e','f']))




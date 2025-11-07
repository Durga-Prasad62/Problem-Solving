# rows,cols = map(int,input().split())
# mat = []
# for _ in range (rows):
#     row = list(map(int,input().split()))
#     mat.append(row)
# left_sum = 0
# right_sum = 0 
# for i  in range(rows):
#     for j in range(cols):
#         if i == j:
#             left_sum += mat[i][j]
#         if i+j == cols-1:
#          right_sum += mat[i][j]
# print("left diagonal sum",left_sum)
# print("right diagonal sum",right_sum)




# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# countA=0
# countB=0
# for i in range(len(A)):
#     for j in range(len(B)):
#         if A[i]>B[j]:
#             countA+=1
#             A[i]=0
#         else:
#             countB+=1
# print("A wins",countA ,"Times")

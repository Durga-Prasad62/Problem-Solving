#Basic Matrix Programs

#addition of two matrices
A = [[1,2],
     [3,4]]
B = [[5,6],
     [7,8]]
C = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        res=(A[i][j]+B[i][j])
        row.append(res)
    C.append(row)  
print(C)
# [[6, 8], [10, 12]]

#substraction of two matrices
A = [[9,8],
     [7,6]]
B = [[1,2],
     [3,4]]
C = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        res = (A[i][j]-B[i][j])
        row.append(res)
    C.append(row)
    
print(C)
# [[8, 6], [4, 2]]

#Transpose of matrix
A = [[1,2],
     [3,4],
     [5,6]]
T = []
for i in range(len(A[0])):
    C = []
    for j in range(len(A)):
       C.append(A[j][i])
    T.append(C)
    
print(T)
# [[1, 3, 5], [2, 4, 6]]



  



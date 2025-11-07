rows,cols = map(int,input().split())
matrix=[]
for i in range(rows):
    row= list( map(int,input().split()))
    matrix.append(row)
#perform Row Sum on this
rowsum=[]
for i in range(rows):
    sum = 0
    for j in range(cols):
        sum += matrix[i][j]
    rowsum.append(sum)
print(rowsum)
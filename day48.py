# Matrix Rotation 
m = [[1,4,6,7],
     [3,6,7,8],
     [8,7,3,4]
    ]
for i in range(len(m[0])): 
    for j in range(len(m)-1,-1,-1):
       print( m[j][i],end=" ")
    print()

# output
# 8 3 1 
# 7 6 4 
# 3 7 6
# 4 8 7 


# #identity matrix   1  0  0
#                    0  1  0
#                    0  0  1

#identity matrix rules diagonals i == j are in 1 and  remaining zero then only satfies
rows,cols = map(int,input().split())
Mat = []
if rows != cols: #check square matrix or not
   print("its not a square matrix")
else:
  for i in range(rows):
    row = list(map(int,input().split()))
    Mat.append(row)
  is_identity = True
  for  i in range(rows):
    for j in range(cols):  #if rules not obey set flag false and break 
      if i == j and Mat[i][j] != 1  or  i!= j and Mat[i][j]!=0:
        is_identity = False
        break
    if not is_identity:#early violation
       break
  if is_identity:
      print("Identity Matrix")
  else:
      print("Not  a Identity Matrix")


# output
# 1 0 0
# 0 1 0 
# 0 0 1
# Identity Matrix
  

    
      





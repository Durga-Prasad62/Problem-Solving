ls = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(ls)):
    for j in range(len(ls)-1):
        if ls[j][1] > ls[j+1][1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]
print(ls)

#with inbuilt method
ls = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
ls.sort(key=lambda x:x[1])
print(ls)

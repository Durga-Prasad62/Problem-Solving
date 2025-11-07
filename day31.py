
#intersection of lists
ls1 =list(map(int,input().split()))
ls2 = list(map(int,input().split()))
nls=[]
for i in range(len(ls1)):
    for j in range(len(ls2)):
        if  ls1[i]==ls2[j]:
            nls.append(ls2[j])
        
print(sorted(set(nls)))

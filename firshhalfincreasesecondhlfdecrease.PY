ls = [8,7,1,6,5,9]
for i in range(len(ls)):
    for j in range(len(ls)-i-1):
        if ls[j]>ls[j+1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]
low = len(ls)//2
high = len(ls)-1
while(low<high):
    if ls[low]<ls[high]:
        ls[low],ls[high]= ls[high],ls[low]
        low+=1
        high-=1
print(ls)
#Roman number To Decimal
n=input("enter a roman number:")
d={'I':1,'V':5, 'X':10,'L':50,'C':100,'D':500 ,'M':1000}

sum=0
for i in  range(len(n)):
    if i <len(n)-1 and  d[n[i]] <d[n[i+1]] :
        sum-=d[n[i]] 
    else:
        sum+=d[n[i]]
print(sum)

        

   
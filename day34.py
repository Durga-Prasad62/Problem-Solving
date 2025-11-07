l=[3, 2, 2, 3, 4]
mean=sum(l)/len(l)
print("mean is :",mean)
mode_list=[]
max_count=0
for i in l:
    count=0
    for j in l:
        if i ==j:
            count+=1
    if count>max_count:
     max_count=count
     mode_list=[i]
    elif count==max_count and i not in mode_list:
       mode_list.append(i)
print("mode is", mode_list)  
l.sort()#sorted is[2, 2, 3, 3, 4]
if len(l)%2==1:
   m=len(l)//2
   
   print("median is",l[m])  #for even middle1 = len(list)//2 - 1    
                            # middle2 = len(list)//2
                             # Median = (list[middle1] + list[middle2]) / 2)



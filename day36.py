def single_element(arr): #without using count
    ul=[]
    if len(arr)==1:
        ul.append(arr[0])
        print(arr)
    else:
        for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    if arr[i]>arr[j]:
                        arr[i],arr[j]=arr[j],arr[i]
        if arr[0]!=arr[1]:
            ul.append(arr[0])
        elif arr[-1]!=arr[-2]:
                ul.append(arr[-1])
        for i in range(1,len(arr)-1):
            if  arr[i] != arr[i-1] and arr[i] != arr[i+1]:
                    ul.append(arr[i])
        print(ul)
l1=[1]
l2=[1,2,2,1,2,4]
l3=[5,6,4,2,3,3,2,4,6]
single_element(l1)
single_element(l2)
single_element(l3)

# ls=[1]
# for i in ls:
#     count=0
#     for j in ls:
#         if i==j:
#             count+=1
#     if count==1:
#         print(j)
#         break




  
    

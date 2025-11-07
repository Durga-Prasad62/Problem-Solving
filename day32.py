
#missing  number
def missing_number(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    expected=1
    for k in range(len(arr)):
        if arr[k]<1:
            continue
        if arr[k]==expected:
            expected+=1
        else:
            print(expected)
            break
    else:
        print(expected)
list1=[]
list2=[1,2,3,4,6]
list3=[1,2,4,0,-1,-2]
list4=[1,2,3,4,5,6]
missing_number(list1)
missing_number(list2)
missing_number(list3)
missing_number(list4)





            

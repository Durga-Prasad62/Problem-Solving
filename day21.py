# n=5
# for rows in range(1,n):
#     print("  "*(n-rows)+"* "*(2*rows-1))
# for rows in range(n-2,0,-1):
#     print("  "*(n-rows)+"* "*(2*rows-1))z+







# str1=(input("enter a string:"))
# count=1
# res=""
# for i in range(1,len(str1)):
#     if str1[i]==str1[i-1]:
#        count+=1
#     else:
#         res+=str1[i-1]+str(count)
#         count=1
# res+=str1[-1]+str(count)
# print(res)




# def Run_Length_encoding(str1):
#     count=1
#     res=""
#     for i in range(1,len(str1)):
#         if str1[i]==str1[i-1]:
#          count+=1
#         else:
#             res+=str1[i-1]+str(count)
#             count=1
#     res+=str1[-1]+str(count)
#     print(res)
# Run_Length_encoding("aabbcc")
# Run_Length_encoding("abababacc")
# Run_Length_encoding("aabbbcca")
# Run_Length_encoding("abc")
# Run_Length_encoding("a")


def Run_Length_encoding(str1):
    count=1
    res=""
    for i in range(len(str1)):
        if i<len(str1)-1  and str1[i]==str1[i+1]:
         count+=1
        else:
            res+=str1[i]+str(count)
            count=1
    print(res)
Run_Length_encoding("aabbcc")
Run_Length_encoding("abababacc")
Run_Length_encoding("aabbbcca")
Run_Length_encoding("abc")
Run_Length_encoding("a")



# n=10
# for rows in range(1,n+1):
#     for cols in range(1,n+1):
#        if rows%2==1 and (rows+cols)%2==0:
#           print("*",end=" ")
#        elif rows==2 and(cols==3 or cols==5):
#           print("*",end=" ")
#        elif rows==4 and(cols==1 or cols==3):
#           print("*",end=" ")
#        else:
#           print(" ",end=" ")
#     print()




        



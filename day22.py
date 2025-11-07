# frequency of char
# str1="banana"
# for i in str1:
#     count=0
#     for j in str1:
#         if i==j:
#             count+=1
#     print(i,count ,end=" ")




#spy number between 100 to 10000
# for example  123  sum and product is 6 

# for i in range(100,10000):
#    single=i
#    sum=0
#    prod=1
#    while(single!=0):
#       rem=single%10
#       sum+=rem
#       prod*=rem
#       single//=10
#    if sum==prod:
#       print(i)




# num=int(input("enter a number"))
# rev=0
# temp=num
# count=1
# while(temp!=0):
#     rem=temp%10
#     rev=rev+rem**count
#     count+=1
#     temp//=10
#     print(rev)
# if num==rev:
#     print("Disarium number")
# else:
#     print("not a disarium")



#nearest palindrome 123  121 o/p
#smallest missing positive number
# lst=[3,1,-1,0]
# for i in  range(len(lst)):
#     lst.sort()
#     lst.insert(2,2)
# print(lst)




#0
#1 3
#1 5 13
#2 8 21 34


n=4
a,b=0,1
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(a,end=" ")
        a,b=b,a+b
    print()











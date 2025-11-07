# binary="11100011100001111100"
# start=0
# max_len=0
# for i in range(len(binary)):
#     end=i
#     if binary[i]!='1':
#         start=i+1
#     else:
#         length=end-start+1
#         if  length>max_len:
#             max_len=length
# print(max_len)


# def strong_check(num):
#     temp=num
#     sum=0
#     while(temp!=0):
#         rem=temp%10
#         temp//=10
#         fact=1
#         for i in range(1,rem+1):
#             fact*=i 
#         sum+=fact
#     return sum==num
# start=int(input("enter a starting number"))
# end=int(input("enter a ending number"))
# for i in range(start,end+1):
#     if strong_check(i):
#         print(i)




# def perfect_number(num):
#     sum=0
#     for i in range(1,num//2+1):
#         if num%i==0:
#             sum+=i
#     return sum==num
# start=int(input("enter starting number:"))
# end=int(input("enter ending number:"))
# for j in range(start,end+1):
#     if perfect_number(j):
#             print(j)
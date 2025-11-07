# n = 5
# for row in range(n):
#     for col in range(n):
#        if row == 0 or col == 0 or col == n-1 or row==n//2:
#            print("*",end=" ")
#        else:
#         print(" ",end=" ")
#     print()


# * * * * * 
# *       * 
# * * * * *
# *       *
# *       *

# n = 5
# for row in range(n):
#     for col in range(n):
#        if row == 0 or col == 0 or col == n-1 or row==n//2 or row == n-1:
#            print("*",end=" ")
#        else:
#         print(" ",end=" ")
#     print()

# # * * * * * 
# # *       * 
# # * * * * *
# # *       *
# # * * * * *


# n = 5
# for row in range(n):
#     for col in range(n):
#        if row == 0 or col == 0 or row == n-1:
#            print("*",end=" ")
#        else:
#         print(" ",end=" ")
#     print()

# * * * * * 
# *
# *
# *
# * * * * *


# n = 4
# a = 0
# b = 1
# for row in range(n):
#     for col in range(1,row+1):
#         print(a,end=" ")
#         c = a+b
#         b = a
#         a = c
#     print()



def fibo(n):
    if  n == 0:
        return  0
    elif n == 1:
        return 1
    return fibo(n-1)+fibo(n-2)
print(fibo(7))
        








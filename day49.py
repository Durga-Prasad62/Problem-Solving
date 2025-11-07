# #Basic Recursion Program

# # Print first n natural numbers using recursion.
def natural(n):
    if n == 0:
        return 
    print(n)
    natural(n-1)

# natural(5)
# output 5
#        4
#        3
#        2
#        1

# # # N natural numbers using recursion in reverse order
def natural(n):
    if n == 0:
        return
    natural(n-1)
    print(n)

natural(5)
# output
# 1
# 2
# 3
# 4
# 5


# # First n even numbers using recursion

def even_number(n):
    if n == 0:
        return
    even_number(n-1)
    if n&1==0:
     print(n)
even_number(10)

# 2
# 4
# 6
# 8
# 10


# Factorial of a number
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)  
print(fact(5))

# 120

# Sum of First N Natural Numbers using Recursion
def sum(n):
    if n == 1:
        return 1
    return n+sum(n-1)  
print(sum(10))
# 55

#sum of each digits
def sum_digits(n):
   if n == 0:
      return 0
   return n%10+sum_digits(n//10) 
print(sum_digits(1234))
# 10



   





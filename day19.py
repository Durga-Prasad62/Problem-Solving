# 🔢 Number-based Carry Forward

# Digit Sum with Carry
# Take a number and keep summing its digits. If the sum is greater than 9, carry forward the excess as a new number and continue until a single digit remains.

# Example: 987 → 9+8+7=24 → carry forward 24 → 2+4=6.






#using string conversing
# def carry_forward(num):
#     sum=0
#     for i in str(num):
#         sum=int(i)+sum
#     carry=0
#     for j in str(sum):
#         carry=int(j)+carry
#     print(carry)
# carry_forward(986)
# carry_forward(985)
# carry_forward(585)








# number system property
# def carry_forward(num):
#     sum=0
#     while(num!=0):
#         rem=num%10
#         num//=10
#         sum+=rem
#     carry=0
#     while(sum!=0):
#         r=sum%10
#         sum//=10
#         carry+=r
#     print(carry)
# carry_forward(987)
# carry_forward(156)
# carry_forward(455)











# def digital_root(num):
#     while num >= 10:   # repeat until single digit
#         s = 0
#         while num > 0:
#             s += num % 10
#             num //= 10
#         num = s
#     return num

# print(digital_root(987))  
# print(digital_root(156)) 
# print(digital_root(455))  
# print(digital_root(9999)) 






    
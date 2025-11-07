# Question: Write a function to convert a string to a number (without using parseInt or Number).
# Testcase: "123"
# Output: 123
# Explanation: The string "123" is converted to the number 123.

# def str_to_int (str1):
#     num=0
#     for ch in str1:
#         digit=ord(ch)-ord('0')
#         num=num*10+digit
#     return num

# print(str_to_int("123"))
# print(str_to_int("456"))


# def str_to_int(str1):
#     num_str = ""         
#     for i in str1:
#         digit = int(i)     
#         num_str += str(digit) 
#     return int(num_str)    

# n = str_to_int("123")
# print(n)            






# def Prime_num(m,n):
    
#     for i in range(m,n+1):
#         if i<2:
#             continue
#         count=0
        
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 count+=1
#                 break
#         if count==0:
#             print(i,end=" ")
#     print()
# Prime_num(1,100)
# Prime_num(100,500)
# Prime_num(500,1000)





def Armstrong_num(m,n):  
    for i in range(m,n+1):
     updated=i
     arm=0
     length=len(str(i))
     temp=i #for safer
     while(temp!=0):
        rem=temp%10
        arm=arm+rem**length
        temp//=10
     if updated==arm:
      print(arm,end=" ")
    print()
Armstrong_num(1,500)
Armstrong_num(100,10000)

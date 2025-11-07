# Nearest ARMSTRONG
def Nearest_Armstrong(num):
    temp,arm=num,0
    count=len(str(num))
    while(temp!=0):
        rem=temp%10
        arm=arm+rem**count
        temp//=10
    return num==arm
input_num=int(input("enter a number:"))
if Nearest_Armstrong(input_num):
        print(input_num)
else:
        left=input_num-1
        right=input_num+1
        while(True):
            if Nearest_Armstrong(left):
                print(left)
                break
            if Nearest_Armstrong(right):
                print(right)
                break
            left-=1
            right+=1


#shortest word in a sentence
# def shortest_word(str1):
#     word=""
#     short=""
#     for i in str1:
#         if i!=" ":
#             word+=i
#         else:
#             if short=="" or len(short)>len(word):
#                 short=word
#             word=""
            
#     print(short)
# shortest_word("I Love Python")
# shortest_word("Python is a Programming Language")
# shortest_word("could you pass the pen")


        

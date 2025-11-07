
def palindrome(num):
    temp=num
    rev=0
    while(temp!=0):
        rem=temp%10
        rev=rev*10+rem
        temp//=10
    return rev==num
input_num=int(input("enter number:"))
if palindrome(input_num):
        print(input_num)
else:
        left=input_num-1
        right=input_num+1
        while True:
            if palindrome(left):
                print(left)
                break
            if palindrome(right):
                print(right)
                break
            left=left-1
            right=right+1
  



def palindrome(num):
    temp=num
    rev=0
    while(temp!=0):
        rem=temp%10
        rev=rev*10+rem
        temp//=10
    if rev==num:
        return rev
start=int(input("enter start number:"))
end=int(input("enter end number:"))
for i in range(start,end+1):
    if palindrome(i):
        print(i,end=" ")
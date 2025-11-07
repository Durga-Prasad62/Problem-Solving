def palindrome_range(num):
    temp = num
    updated = num
    rev =0
    while(temp!=0):
        rem = temp%10
        rev =rev*10+rem
        temp//=10
    return updated == rev
minimum = int(input("enter a min number:"))
maximum = int(input("enter a  max number:"))
for i in range(minimum,maximum+1):
    if palindrome_range(i):
        print(i,end=" ")
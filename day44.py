# n=15
# lst=[]
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         word="FizzBuzz"
#         lst.append(word)
#     elif i%3==0:
#         word="Fizz"
#         lst.append(word)
#     elif i%5==0:
#         word="Buzz"
#         lst.append(word)
#     else:
#         lst.append(i)

# print(lst)



def Dup_list_item(num):
    m = str(num)
    for j in range(len(m)):
        for k in range(j+1,len(m)):
            if m[j] == m[k]:
                return True
    return False

ls = [202,89,112,88]
nls = []
for i in ls:
    nls.append(Dup_list_item(i))
print(nls)
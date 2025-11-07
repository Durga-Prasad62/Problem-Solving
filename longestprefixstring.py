lst = ["apple","ape","april"]
smallest = lst[0]
res=""
for i in lst:
    if i<smallest:
        smallest = i
stop = False
for j in range(len(smallest)):
    for i in lst:
        if smallest[j] == i[j]:
          pass
        else:
            stop = True
            break
        
    if stop:
        break
    else:
          res+=smallest[j]
print(res)
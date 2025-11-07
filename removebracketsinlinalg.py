def remove_brackets(s):
    exp=""
    for i in s:
        if i not in"()[]":
            exp += i
    return exp
print(remove_brackets("a+((b-c)+d)"))
def remove_whitespace(str1):
    result =""
    for ch in str1:
        if ch!=" ":
            result+=ch
    return result
print (remove_whitespace("Going To Home"))

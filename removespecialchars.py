def remove_special_chars(word):
    result = ""
    for i in word:
        if 'A'<=i<='Z' or 'a'<=i<='z':
            result+=i
    return result
print(remove_special_chars("Java&C++"))
#panagram
# The quick brown fox jumps over the lazy dog and the dog jumps again

# str1=input("enter a  string:").lower()
# res="".join(str1.split())
# alpha=list("abcdefghijklmnopqrstuvwxyz")
# is_pangram=True
# for i in alpha:
#     if i  in res:
#      is_pangram=False
#      break


# if is_pangram:
#     print("pangram")
# else:
#     print("not a pangram")





def pangram(str1):
    res="".join(str1.split())
    alpha=list("abcdefghijklmnopqrstuvwxyz")
    is_pangram=True
    for i in alpha:
        if i not  in res:
         is_pangram=False
         break
    if is_pangram:
        print("pangram")
    else:
        print("not a pangram")
pangram("The quick brown fox jumps over the lazy dog and the dog jumps again")
pangram("Hello World")
pangram("she sells seashells on the sea shore")
pangram("pack my box with five dozen liquor jugs")








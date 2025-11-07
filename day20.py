def clean_string(s):
    """Remove spaces and special characters, keep only alphanumeric, and lowercase.""" 
    cleaned = ""
    for ch in s:
        if ch.isalnum():   # keep only letters & digits
            cleaned += ch.lower()
    return cleaned 
def Anagram(str1,str2):
    str1=clean_string(str1)
    str2=clean_string(str2)
    ls1=list(str1)
    ls2=list(str2)
    if len(str1)!=len(str2):
        print("This is not a Anagram")
    else:
        for i in range(len(ls1)):
            for j in range(i+1,len(ls1)):
             if ord(ls1[i])>ord(ls1[j]):
                ls1[i],ls1[j]=ls1[j],ls1[i]
        for i in range(len(ls2)):
            for j in range(i+1,len(ls2)):
             if ord(ls2[i])> ord(ls2[j]):
                ls2[i],ls2[j]=ls2[j],ls2[i]
        if ls1==ls2:
         print("it is a Anagram ")
        else:
            print("it is not  a Anagram ")
Anagram("listen!","silent!")
Anagram("hello","world")
Anagram("evil",'vile')
Anagram("java","python")











 
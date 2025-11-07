
# From a list of words, create another list with only words that are palindromes
def palindrome_list(arr):
    pal_list=[]
    for i in arr:
        if(i.lower()==i[::-1].lower()):
            pal_list.append(i)
    print(pal_list)
list1=["madam","kerala","racecar","panama"]
list2=["hello","Radar","world","Deed"]
list3=["Test","string","Pop","Variable","stats"]
list4=["Refer","noon","Algorithm","Function"]
palindrome_list(list1)
palindrome_list(list2)
palindrome_list(list3)
palindrome_list(list4)




  
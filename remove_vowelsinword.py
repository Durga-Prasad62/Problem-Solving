def  remove_vowels_in_word(word):
    vowels="AaEeIiOoUu"
    res=""
    for i in word:
        if i not in vowels:
            res+=i
    return res
print(remove_vowels_in_word("Forward"))



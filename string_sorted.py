#  input  : cedfzvba
#  output : abcdefvz

def String_sort(alphabets):
    s_list=list(alphabets)
    for i in range(len(s_list)):
        for j in range(len(s_list)-i-1):
            if ord ( s_list[j])>ord(s_list[j+1]):
                s_list[j],s_list[j+1] = s_list[j+1] ,s_list[j]
    return "".join(s_list)

print(String_sort( "cedfzvba"))



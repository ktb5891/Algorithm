def solution(str1, str2):
    answer = 0
    str1,str2 = str1.lower(),str2.lower()
    li1 = []
    li2 = []
    str1,str2 = ''.join(filter(str.isalnum, str1)),''.join(filter(str.isalnum, str2))
    print(str1,str2)
    str1,str2 = ''.join(filter(str.isalpha, str1)),''.join(filter(str.isalpha, str2))
    print(str1,str2)
    for i in range(len(str1)-1):
        li1.append(str1[i]+str1[i+1])
        try:
            int(i)
        except ValueError:
            li1.pop()
    for i in range(len(str2)-1):
        li2.append(str2[i]+str2[i+1])
        try:
            int(i)
        except ValueError:
            li2.pop()
    mom = len(set(li1+li2))
    son = 0
    for i in li1:
        if i in li2:
            son += 1
            
    if mom == 0:
        result = 1
    else:
        result = son/mom
    
    print(son,mom)
    answer = int(65536*result)
    print(li1,li2)
    return print(answer)

str1 = 'aa1+aa2'
str2 = 'AAAA12'
solution(str1,str2)
def solution(s):
    answer = []
    s = list(s)
    for i in range(len(s)):
        if s[i] == '{':
            s[i] = '['
        elif s[i] == '}':
            s[i] = ']'
    s = "new_s = "+"".join(s)
    s += '''
n = 0
length = 1

while new_s:

    if len(new_s[n]) == length:
        for i in answer:
            new_s[n].remove(i)
        answer.append(new_s[n][0])
        new_s.pop(n)
        n = 0
        length += 1


    else:
        n += 1
           
    '''

    exec(s)
    
    
    return print(answer)
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
solution(s)
n = int(input())
m = 1
for num in range(n+1):
    str_list = []
    for i in range(n+1,m,-1):
        str_list.append(' ')
    for j in range(m-1):
        str_list.append('*')
    m += 1
    if '*' not in str_list:
        continue
    print(''.join(str_list))

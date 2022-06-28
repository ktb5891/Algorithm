n = int(input())
ans = []
for _ in range(n):
    count, string = input().split(' ')
    temp = ''
    for s in string:
        for i in range(int(count)):
            temp += s
    ans.append(temp)
for _ in ans:
    print(_)

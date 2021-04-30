n, s, m = map(int, input().split(' '))

v = [int(x) for x in input().split()]

# print(v)

dp1 = [0 for _ in range(m+1)]
dp2 = [0 for _ in range(m+1)]

dp1[s] = 1

for i in v:
    for j in range(m+1):
        if dp1[j]:
            if i+j <= m:
                dp2[j+i] = 1
            if j-i >= 0:
                dp2[j-i] = 1
    dp1 = dp2
    dp2 = [0]*(m+1)

answer = -1
for i in range(m,-1,-1):
    if dp1[i]:
        answer = i
        break
print(answer)

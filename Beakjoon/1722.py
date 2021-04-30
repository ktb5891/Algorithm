n = int(input())
k = [int(x) for x in input().split()]
fac = [0,1]

def factorial_list(n,fac_list):
    for i in range(2,n+1):
        fac_list.append(fac_list[i-1]*i)
    return fac_list

fac = factorial_list(n,fac)
# print(fac)
if k[0] == 1:
    m = k[1]-1
    num = n-1
    k = [i for i in range(1,n+1)]
    ans = []
    for i in range(n-1):
        ans.append(k[m//fac[num]])
        del k[m//fac[num]]
        m %= fac[num]
        num -= 1
    ans.append(k[0])
    ans = map(str,ans)
    print(' '.join(ans))
else:
    ans = 0
    k = k[1:]
    num = n-1
    for i in range(n):
        count = 0
        for j in range(i, n):
            if i == j:
                continue
            if k[i] > k[j]:
                count += 1
        for l in range(count):
            ans += fac[num]
        num -= 1
    print(ans+1)
    

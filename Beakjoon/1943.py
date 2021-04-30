ans = []

for _ in range(3):
    money = 0
    dp = [0 for i in range(50001)]
    coin = [[] for i in range(101)]
    num = int(input())
    # print(coin)
    for i in range(1,num+1):
        a, b = map(int,input().split())
        money += a*b
        coin[i] = [a,b]
    # print(coin)
    # print(money)
    if money%2 == 1:
        ans.append(0)
    else:
        dp[0] = 1
        for i in range(1,num+1,1):
            for j in range(50000,coin[i][0]-1,-1):
                if dp[j-coin[i][0]]:
                    k=0
                    while k < coin[i][1] and j+k*coin[i][0] <= 50000:
                        dp[j+k*coin[i][0]] = 1
                        k += 1
        ans.append(dp[int(money/2)])
        # print(dp)
for i in ans:
    print(i)
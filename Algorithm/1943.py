ans = []
for _ in range(3):
    num = int(input())
    dic = dict()
    for i in range(num):
        coin, x = map(int, input().split())
        dic[coin] = x
    # print(dic[coin])
    sort_dic = sorted(dic.items())
    # print(sort_dic)
    money = [0,0]
    while sort_dic:
        k = list(sort_dic.pop())
        # print(k)
        if money[0] == money[1]:
            if k[1]%2 == 0:
                money[0] += k[0]*(k[1]/2)
                money[1] += k[0]*(k[1]/2)
            else:
                while k[1] > 0:
                    if money[0] == money[1]:
                        money[0] += k[0]
                        k[1] -= 1
                    elif money[0] > money[1]:
                        money[1] += k[0]
                        k[1] -= 1
                    elif money[0] < money[1]:
                        money[0] += k[0]
                        k[1] -= 1
        else:
            while k[1] > 0:
                    if money[0] == money[1]:
                        money[0] += k[0]
                        k[1] -= 1
                    elif money[0] > money[1]:
                        money[1] += k[0]
                        k[1] -= 1
                    elif money[0] < money[1]:
                        money[0] += k[0]
                        k[1] -= 1
    # print(money)
    if money[0] == money[1]:
        ans.append(1)
        # print(ans)
    else:
        ans.append(0)
        # print(ans)
    
for i in ans:
    print(i)
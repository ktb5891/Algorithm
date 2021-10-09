n = int(input())
map_dic = {}
for i in range(n):
    map_dic[i] = list(map(int,input().split()))
print(map_dic)
k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            map_dic[i][j] = map_dic[i][j] + map_dic[i - 1][j]
        elif i == j:
            map_dic[i][j] = map_dic[i][j] + map_dic[i - 1][j - 1]
        else:
            map_dic[i][j] = max(map_dic[i - 1][j - 1], map_dic[i - 1][j]) + map_dic[i][j]
    k += 1

print(max(map_dic[n-1]))

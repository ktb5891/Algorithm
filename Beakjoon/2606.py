n = int(input())
m = int(input())
way = {idx : [] for idx in range(n)}
for i in range(m):
    start, end = map(int,input().split())
    way[start-1].append(end-1)
    # way[end].append(start)
print(way)

virus = [0 for i in range(n)]

def dfs(v):
    virus[v] = 1
    for i in range(n):
        if i in way[v] and virus[i] == 0:
            dfs(i)

dfs(0)
print(virus.count(1)-1)
n,m,k = map(int, input().split())

spot = [[0]*m for _ in range(n)]
# print(spot)
dxy = []
for i in range(k):
    r,c = map(int, input().split())
    spot[r-1][c-1] = 1
    dxy.append((r-1,c-1))
# print(dxy)
# print(spot)
ans = 0
check = [[False]*m for _ in range(n)]
while dxy:
    i, j = dxy.pop()
    if check[i][j]:
        continue
    count = 1
    check[i][j] = 1
    new_dxy = [(i,j)]
    while new_dxy:
        i, j = new_dxy.pop()
        for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0 <= x < n and 0 <= y < m:
                if not check[x][y] and spot[x][y] == 1:
                    check[x][y] = 1
                    count += 1
                    new_dxy.append((x,y))
    ans = max(ans,count)
print(ans)

n, m = map(int,input().split())
ball_li = [i+1 for i in range(n)]
for _ in range(m):
    i,j = map(int,input().split())
    temp = ball_li[i-1]
    ball_li[i-1] = ball_li[j-1]
    ball_li[j-1] = temp
ball_li = list(map(str,ball_li))
print(' '.join(ball_li))
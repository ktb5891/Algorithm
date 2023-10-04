n,m = map(int,input().split())
ball_li = [0]*n
for i in range(m):
    start, end, ball = map(int,input().split())
    for j in range(start-1,end):
        ball_li[j] = ball
ball_li = list(map(str,ball_li))
print(' '.join(ball_li))
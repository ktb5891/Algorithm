start, end = map(int, input().split(' '))

que = []

visit_que = [0 for _ in range(100001)]

depth = []

depth.append(0)
que.append(start)

while True:
    a = que.pop(0)
    ad = depth.pop(0)

    if visit_que[a] != 1:
        visit_que[a] = 1

        if a-1 >= 0:
            que.append(a-1)
            depth.append(ad+1)

        if 2*a <= 100000:
            que.append(2*a)
            depth.append(ad+1)

        if a+1 <= 100000:
            que.append(a+1)
            depth.append(ad+1)

    if a == end:
        print(ad)
        break
        

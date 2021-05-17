# import numpy as np
from collections import deque
w,h = map(int,input().split())
while w != 0 and h != 0:
    map_s = [[] for _ in range(h)]
    for i in range(h):
        map_s[i] = input().split()
        map_s[i] = list(map(int,map_s[i]))

    visited = deque()
    answer = 0
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for i in range(h):
        for j in range(w):
            if map_s[i][j] == 1:
                map_s[i][j] = 0
                visited = deque([[i,j]])
                while visited:
                    root_x, root_y = visited[0][0], visited[0][1]
                    visited.popleft()
                    for k in range(8):
                        x = root_x+dx[k]
                        y = root_y+dy[k]
                        if 0 <= x < h and 0<= y < w and map_s[x][y] == 1:
                            map_s[x][y] = 0
                            visited.append([x,y])
                answer +=1

    print(answer)

    w,h = map(int,input().split())

# import numpy as np
# aa = np.array((1,2))
# bb = (1,2)
# print(bb[0]+1)
# print(aa+1)

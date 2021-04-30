num = int(input())

def sel_rgb(N):
    if N == 0:
        return 'R'
    elif N == 1:
        return 'G'
    elif N == 2:
        return 'B'

rgb_list = [[0,0,0] for _ in range(num)]
for i in range(num):
    rgb_list[i] = list(map(int, input().split(' ')))
    
# print(rgb_list)
rgb = 'S'
rgb_1 = 'S'

answer = 0
sett = []
for i in range(num):
    if rgb == 'S':
        temp = rgb_list[i].index(min(rgb_list[i]))
        rgb = sel_rgb(temp)
        sett.append(rgb)
        answer += min(rgb_list[i])
    elif rgb_1 == 'S' and rgb_1 == rgb:
        rgb_list[i][temp] = 1001
        temp = rgb_list[i].index(min(rgb_list[i]))
        rgb = sel_rgb(temp)
        sett.append(rgb)
        answer += min(rgb_list[i])
    elif i == num:
        temp = rgb_list[i].index(min(rgb_list[i]))
        rgb = sel_rgb(temp)
        if rgb_1 == rgb:
            rgb_list[i][temp] = 1001
            temp = rgb_list[i].index(min(rgb_list[i]))
            rgb = sel_rgb(temp)
            sett.append(rgb)
            answer += min(rgb_list[i])
    else:
        temp = rgb_list[i].index(min(rgb_list[i]))
        rgb = sel_rgb(temp)
        if sett[i-2] == sett[i-1] and rgb == sett[i-1]:
            rgb_list[i][temp] = 1001
            temp = rgb_list[i].index(min(rgb_list[i]))
            rgb = sel_rgb(temp)
            sett.append(rgb)
            answer += min(rgb_list[i])
            rgb_2 = sett[i-1]
        else:
            temp = rgb_list[i].index(min(rgb_list[i]))
            rgb = sel_rgb(temp)
            sett.append(rgb)
            answer += min(rgb_list[i])
            rgb_2 = sett[i-1]
    rgb_1 = rgb

if answer >= 1000:
    answer = 1000



print(answer)
# print(sett)

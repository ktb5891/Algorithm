case = int(input())

area = [[0,0] for i in range(case)]
len_list = []
for i in range(case):
    a,b = map(int, input().split(' '))
    area[i] = [a,b]
    len_list.append(b-a)
# print(area)
# print(len_list)
answer = [0 for i in range(case)]

for i in range(case):
    move = 1
    move_sum = 0
    while move_sum < len_list[i]:
        answer[i] += 1
        move_sum += move
        if answer[i] % 2 == 0:
            move += 1
    print(answer[i])  

    
            
        


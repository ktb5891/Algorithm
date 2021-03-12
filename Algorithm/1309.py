N = int(input())

answer = 0
set_num = 3
for i in range(N):
    if i == 0:
        answer += 1
    else:
        temp = set_num
        set_num = (2*set_num+answer)%9901
        answer = temp

print(set_num)


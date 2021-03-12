case = int(input())

score = [0 for _ in range(case)]
avg = [0 for _ in range(case)]
count = [0 for _ in range(case)]
for i in range(case):
    score[i] = list(map(int, input().split()))
    avg[i] = sum(score[i][1:])/score[i][0]
    
    for j in score[i][1:]:
        if avg[i] < j :
            count[i] += 1
            # print(avg[i], j, count)
for i in range(case):
    print(str(format(count[i]/score[i][0]*100,".3f"))+"%")    
# print(avg)
# print(case)
# print(score)



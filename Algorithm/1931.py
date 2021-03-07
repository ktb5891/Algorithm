N = int(input())
time = [[0]*2 for i in range(N)]
# end = [0 for i in range(num)]

# for i in range(num):
#     start[i], end[i] = map(int, input().split(' '))
#     time.append(end[i]-start[i])

for i in range(N): 
    s, e = map(int, input().split(' ')) 
    time[i][0] = s 
    time[i][1] = e 
# print(time)

time.sort(key = lambda x: (x[1], x[0]))
# print(time)
cnt = 1 
end_time = time[0][1] 
for i in range(1, N): 
    if time[i][0] >= end_time: 
        cnt += 1 
        end_time = time[i][1] 

print(cnt)



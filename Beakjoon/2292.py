n = int(input())

bh_num = 1 
cnt = 1
while n > bh_num :
    bh_num += 6 * cnt
    cnt += 1
print(cnt)
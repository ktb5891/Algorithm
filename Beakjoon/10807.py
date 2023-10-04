n = int(input())
num_li = list(map(int,input().split()))
find_num = int(input())
count = 0
for i in num_li:
    if i == find_num:
        count += 1

print(count)
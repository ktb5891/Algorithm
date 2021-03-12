num, wifi = map(int, input().split(' '))

home = [0 for _ in range(num)]
for i in range(num):
    home[i] = int(input())

home.sort()

start = 1
end = home[-1] - home[0]
answer = 0
while start <= end:
    mid = (start+end)//2
    first = home[0]
    count = 1

    for i in range(1, num):
        if home[i] >= first+mid:
            count += 1
            first = home[i]

    if count >= wifi:
        start = mid+1
        answer = mid
    else:
        end = mid-1

print(answer)

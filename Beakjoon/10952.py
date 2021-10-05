a,b = -1, -1

while a != 0 and b != 0:
    a,b = map(int,input().split())
    sum = a+b
    if sum == 0:
        break
    print(sum)

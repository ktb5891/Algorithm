n, want = map(int,input().split())
tree = list(map(int,input().split()))
left = 1
right = max(tree)
while left <= right:
    target = (left+right)//2
    sum = 0
    print('tg',target)
    for i in tree:
        if i > target:
            sum += i-target
    print(sum)
    print('left, right',left,right)
    if sum >= want:
        left = target+1
        print('if',left)
    else:
        right = target-1
        print('else',right)
        

print(right) 
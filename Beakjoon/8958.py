n = int(input())
ans = []
def summ(num1,num2):
    if num2 == 0:
        return num1
    else:
        num2 -= 1
        num1 = num1+num2
        return summ(num1,num2)
for _ in range(n):
    score = [x for x in input().split('X')]
    # print(score)
    count = 0
    for i in score:
        count += summ(len(i),len(i))
    ans.append(count)
for i in ans:
    print(i)
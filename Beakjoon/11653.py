N = int(input())

div = 2
div_list = []
while True:
    if N == 1:
        break
    elif N%div == 0:
        N //= div
        div_list.append(div)
    else:
        div += 1
for i in div_list:
    print(i)
    
N,X = map(int,input().split())

n_array = []
n_array = list(map(int,input().split()))
answer = []
for i in n_array:
    if i < X:
        answer.append(i)
answer = list(map(str,answer))
print(' '.join(answer))
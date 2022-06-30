a,b,c = map(int, input().split(' '))

def sol(a,b,c):
    if c <= b:
        return print(-1)
    else:
        return print(int(a/(c-b)+1))

sol(a,b,c)

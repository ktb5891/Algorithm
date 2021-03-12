a,b,c = map(int,input().split(' '))

def ans(a,b):
    if b == 1:
        return a%c
    else:
        x = ans(a,b//2)
        if b%2 == 0:
            return x*x%c
        else:
            return x*x*a%c

answer = ans(a,b)
print(answer)
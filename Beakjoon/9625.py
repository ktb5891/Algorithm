n = int(input())
a = 0
b = 1

def solution(a,b,n):
    if n > 1:
        new_b = a+b
        new_a = b
        a = new_a
        b = new_b
        n -= 1
        return solution(a,b,n)
    else:
        return print(a,b)
solution(a,b,n)
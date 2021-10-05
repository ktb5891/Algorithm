from sys import stdin
num = int(stdin.readline())

def factorial(num):
    ans = 1
    if num > 0:
        ans = num*factorial(num-1)
    return ans
    
print(factorial(num))
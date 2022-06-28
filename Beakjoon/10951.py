try:
    while True:
        num1, num2 = map(int,input().split(' '))
            
        if num1 > 0 and num2 < 10:
            print(num1+num2)

        else:
            break
except EOFError:
    pass
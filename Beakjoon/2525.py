hour, minu = map(int, input().split(' '))
cook = int(input())

minu = minu + cook

while minu >= 60:
    minu = minu - 60
    hour += 1
    if hour >= 24:
        hour = hour - 24

print(hour,minu)
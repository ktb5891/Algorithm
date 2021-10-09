n = int(input())

ten = n//10
one = n%10
new_one = ten+one
new_n = one*10+new_one%10
count = 1
while new_n != n:
    ten = new_n//10
    one = new_n%10
    new_one = ten+one
    new_n = one*10+new_one%10
    count += 1
print(count)
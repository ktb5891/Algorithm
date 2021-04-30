size = int(input())
A = [0 for _ in range(size)]
B = [0 for _ in range(size)]
C = [0 for _ in range(size)]
D = [0 for _ in range(size)]
count = 0
for i in range(size):
    A[i], B[i], C[i], D[i] = map(int, input().split(' '))


# for a in A:
#     for b in B:
#         for c in C:
#             for d in D:
#                 if a+b+c+d == 0:
#                     count += 1
#                     print(a,b,c,d)
# print(A,B,C,D)
abcd = dict()
for a in A:
    for b in B:
        abcd[a+b] = abcd.get(a+b,0)+1

for c in C:
    for d in D:
        count += abcd.get(-(c+d),0)

#print(abcd)


print(count)

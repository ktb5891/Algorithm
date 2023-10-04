
n,m = input().split()

list1 = [[0]*int(n)]*int(m)
list2 = [[0]*int(n)]*int(m)
list3 = [[0]*int(n)]*int(m)
list4 = [[0,0,0],[1,1,1],[2,2,2]]

for i in range(int(n)):
    for j in range(int(m)):
        print(list4[i][j])

for i in range(int(n)):
    list1[i] = list(map(int,input().split()))

print(list1)
for j in range(int(n)):
    list2[j] = list(map(int,input().split()))

print(list2)
for k in range(int(n)):
    for v in range(int(m)):
        print('list1 : ',k,v,list1[k][v])
        print('list2 : ',k,v,list2[k][v])
        print(list3)
        list3[k][v] = list1[k][v]+list2[k][v]
        print(list3)
for i in list3:
    print(*i)
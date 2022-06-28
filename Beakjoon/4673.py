def self_num(n):
    st_li = list(str(n))
    int_li = list(map(int,st_li))
    return n+sum(int_li)

num_li = []
for i in range(10000):
    num_li.append(self_num(i))

for i in range(10000):
    if i in num_li:
        pass
    else:
        print(i)
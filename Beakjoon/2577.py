from collections import Counter
a = int(input())
b = int(input())
c = int(input())
n = a*b*c
n_li = list(str(n))
num_dic = {str(i):0 for i in range(10)}

for key in n_li:
    num_dic[key] = Counter(n_li)[key]

for i in range(10):
    print(num_dic[str(i)])

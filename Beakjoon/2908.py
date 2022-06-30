a,b = input().split()
a, b = str(a),str(b)
li_a,li_b = [],[]

for i in range(2,-1,-1):
    li_a.append(a[i])
    li_b.append(b[i])
ans = [''.join(li_a),''.join(li_b)]
print(max(ans))
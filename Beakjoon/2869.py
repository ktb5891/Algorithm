# a,b,v = map(int,input().split())
# day = 1
# def sol(a,b,v,day):
#     if a >= v:
#         return print(day)
#     else:
#         v = v-(a-b)
#         day += 1
#         return sol(a,b,v,day)

# sol(a,b,v,day)

a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)
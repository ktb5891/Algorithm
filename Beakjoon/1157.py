from collections import Counter

s = input().lower()
s_li = list(set(s))
s_dic = {x:0 for x in s}

for i in s:
    s_dic[i] += 1

max_items = []

for i in s_dic.keys():
    if s_dic[i] == max(s_dic.values()):
        max_items.append(i)

if len(max_items) > 1:
    print('?')
else:
    print(max_items[0].upper())
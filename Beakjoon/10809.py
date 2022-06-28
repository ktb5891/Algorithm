s = input()
s = list(s)
alphabet_dic = {'a':-1,'b':-1,'c':-1,'d':-1,'e':-1,'f':-1,'g':-1,'h':-1,'i':-1,'j':-1,'k':-1,'l':-1,'m':-1,'n':-1,'o':-1,'p':-1,'q':-1,'r':-1,'s':-1,'t':-1,'u':-1,'v':-1,'w':-1,'x':-1,'y':-1,'z':-1}
for i in s:
    if alphabet_dic[i] == -1:
        alphabet_dic[i] = s.index(i)
print(' '.join(list(map(str,list(alphabet_dic.values())))))


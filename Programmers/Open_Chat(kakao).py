def solution(record):
    answer = []
    rec_list = []
    new = {}
    seq = []
    for j in record:
        rec_list.append(j.split(" "))
    
    for k in rec_list:
        if k[0] != 'Change':
            seq.append(k[1])
    
    for idx,i in enumerate(rec_list):
        if i[1] not in new.keys():
            new[i[1]] = [i[2],i[0]]
        elif i[0] == 'Change':
            new[i[1]][0] = i[2]
        elif i[0] == 'Enter':
            new[i[1]][0] = i[2]
            new[i[1]].append(i[0])
        else:
            new[i[1]].append(i[0])
    # print(new)
    # print(seq)
    while seq:
        now = seq.pop(0)
        move = new[now].pop(1)
        if move == 'Enter':
            answer.append(new[now][0]+'님이 들어왔습니다.')
        elif move == 'Leave':
            answer.append(new[now][0]+'님이 나갔습니다.')
    return answer
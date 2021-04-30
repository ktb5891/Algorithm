def solution(participant, completion):
    answer_dic = dict()
    for i in participant:
        answer_dic[i] = answer_dic.get(i,0)+1
    for j in completion:
        answer_dic[j] -= 1
    for k in answer_dic:
        if answer_dic[k]:
            answer = k
    return answer
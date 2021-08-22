def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]*2000
    second = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    count = [0 for i in range(3)]
    for i in range(len(answers)):
        if first[i] == answers[i]:
            count[0] += 1
        if second[i] == answers[i]:
            count[1] += 1
        if third[i] == answers[i]:
            count[2] += 1
    maxi = max(count)
    for i,v in enumerate(count):
        if v == maxi:
            answer.append(i+1)
    return answer
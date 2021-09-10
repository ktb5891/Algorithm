def solution(a, b):
    if a == b:
        answer = a
    else:
        answer = 0
        num_list = sorted([a,b])
        for i in range(num_list[0],num_list[1]+1):
            answer += i
    return answer
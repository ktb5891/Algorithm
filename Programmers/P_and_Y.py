def solution(s):
    s = s.lower()
    p_count = s.count('p')
    y_count = s.count('y')
    if p_count == y_count:
        answer = True
    else:
        answer = False
    return answer
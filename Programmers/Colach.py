def solution(num):
    count = 0
    answer = 0
    while num != 1:
        if count == 500:
            answer = -1
            break
        elif num%2 == 0:
            num = num/2
        elif num%2 != 0:
            num = num*3+1
        count += 1
        answer = count
    return answer
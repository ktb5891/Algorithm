from collections import deque
def solution(priorities, location):
    answer = 0
    pri = deque([(priorities[i],i) for i in range(len(priorities))])
    while pri:
        temp = pri.popleft()
        if pri and max(pri)[0] > temp[0]:
            pri.append(temp)
        else:
            answer += 1
            if temp[1] == location:
                break
    return answer
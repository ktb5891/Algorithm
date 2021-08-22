from collections import deque
def solution(begin, target, words):
    answer = 0
    now = begin
    w = deque(words)
    if target not in w:
        pass
    else:
        while w:
            check = 0
            check2 = 0
            next_list = w.popleft()

            for i in range(len(now)):
                if now[i] != next_list[i]:
                    check += 1
                if now[i] != target[i]:
                    check2 += 1
            if check2 == 1:
                answer += 1
                break
            if check != 1:
                w.append(next_list)
                continue
            print(check2,check,answer,now,next_list)
            answer += 1            
            now = next_list
    
    return answer
from collections import deque

def solution(numbers, target):
    answer = 0
    stack = deque([(0, 0)])
    while stack:
        tot, num_idx = stack.popleft()
        if num_idx == len(numbers):
            if tot == target:
                answer += 1
        else:
            num = numbers[num_idx]
            stack.append((tot+num, num_idx + 1))
            stack.append((tot-num, num_idx + 1))

    return print(answer)

numbers = [1,1,1,1,1]
target = 3
solution(numbers,target)
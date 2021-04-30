from collections import deque
def solution(progresses, speeds):
    answer = []
    days = deque([])
    while progresses:
        prog = progresses.pop(0)
        spd = speeds.pop(0)
        for i in range(1,100):
            if prog+spd*i >=100:
                days.append(i)
                break
    print(days)
    before = days.popleft()
    now = days.popleft()
    count = 1
    while True:
        print(days)
        if before >= now:
            count += 1
        else:
            answer.append(count)
            before = now
            count = 1
        if not days:
            answer.append(count)
            break
        now = days.popleft()
    return answer
import heapq as hq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    new_heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                hq.heappush(new_heap, [j[1], j[0]])
        if len(new_heap) != 0:
            current = hq.heappop(new_heap)
            start = now
            now += current[0]
            answer += (now-current[1])
            i +=1
        else:
            now += 1
    return int(answer / len(jobs))
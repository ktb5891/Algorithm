import heapq as hq
def solution(d, budget):
    answer = 0
    hq.heapify(d)
    sel_d = 0
    while d:
        sel_d = hq.heappop(d)
        print(sel_d)
        budget -= sel_d
        if budget >= 0:
            answer += 1
        else:
            budget += sel_d
    return answer
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    length = len(scoville)
    food = heapq.heappop(scoville)
    for i in range(1, length):
        mini = heapq.heappop(scoville)
        food = heapq.heappushpop(scoville, food+mini*2)
        # print(food)
        if food >= K: 
            return i
    # while len(scoville) > 1:
    #     new_food = heapq.heappop(scoville)
    #     if new_food > K:
    #         answer += 1
    #         return answer
    #     else:
    #         new_food += heapq.heappop(scoville)*2
    #         if new_food > K:
    #             answer += 1
    #             return answer
    #         else:
    #             heapq.heappushpop(scoville,new_food)
    #             answer += 1
    # if len(scoville) == 1 and heapq.heappop(scoville) < K:
    #     answer = -1
        
    return -1
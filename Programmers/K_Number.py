import heapq as hq
def solution(array, commands):
    answer = []
    for com in commands:
        start = com[0]-1
        end = com[1]
        find = com[2]
        array2 = array[start:end]
        hq.heapify(array2)
        for f in range(find):
            ans = hq.heappop(array2)
        answer.append(ans)
    return answer
import heapq as hq

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print("0")
    else:
        hq.heappush(heap,[-num,num])
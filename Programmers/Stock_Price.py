from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        count = 0
        now = prices.popleft()
        for i in prices:
            if now > i:
                count += 1
                break
            else:
                count += 1
        answer.append(count)
    return answer
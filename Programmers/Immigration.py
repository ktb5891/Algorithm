def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    while left < right:
        mid = (left+right)//2
        count = 0
        for i in times:
            count += mid//i
        if count >= n:
            right = mid
        else:
            left = mid+1
    answer = left
    return answer
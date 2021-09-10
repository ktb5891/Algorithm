def solution(n):
    water_melon = '수박'
    if n%2 == 0:
        answer = water_melon*(n//2)
    else:
        answer = water_melon*(n//2)+'수'
    return answer
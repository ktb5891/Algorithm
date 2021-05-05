def solution(board, moves):
    answer = 0
    basket = []
    while moves:
        moving = moves.pop(0)
        for i in board:
            if i[moving-1] !=0:
                basket.append(i[moving-1])
                i[moving-1] = 0
                break
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            answer += 2
            basket.pop()
            basket.pop()
    return answer

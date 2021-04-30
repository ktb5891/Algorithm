def solution(n, lost, reserve):
    answer = 0
    
    total_list = [i for i in range(1,n+1)]
    new_lost = []
    while lost:
        i = lost.pop()
        if i in reserve:
            reserve.pop(reserve.index(i))
            continue
        else:
            total_list.remove(i)
            new_lost.append(i)
    while reserve:
        reser = reserve.pop(0)
        print(reser)
        if reser-1 in new_lost:
            total_list.append(new_lost.pop(new_lost.index(reser-1)))
            print("-1",total_list)
            continue
        elif reser+1 in new_lost:
            total_list.append(new_lost.pop(new_lost.index(reser+1)))
            print("+1",total_list)
            continue
    print(total_list)
    answer = len(total_list)
    return answer
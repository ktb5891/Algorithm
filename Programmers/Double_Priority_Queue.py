import heapq as hq
def solution(operations):
    answer = []
    num_list = []
    for i in operations:
        
        if i[0] == 'I':
            hq.heappush(num_list,int(i[2:]))
            
        elif num_list:
            if i[2:] == '-1':
                print('b',num_list)
                hq.heappop(num_list)
                print('a',num_list)
            else:
                print('bb',num_list)
                for j,v in enumerate(num_list):
                    num_list[j] = v*-1
                hq.heapify(num_list)
                print('bb2',num_list)
                hq.heappop(num_list)
                print('aa2',num_list)
                for j,v in enumerate(num_list):
                    num_list[j] = v*-1
                hq.heapify(num_list)
                print('aa',num_list)
    print(num_list)
    if num_list:
        for j,v in enumerate(num_list):
            num_list[j] = v*-1
        hq.heapify(num_list)
        answer.append(hq.heappop(num_list)*-1)
        for j,v in enumerate(num_list):
            num_list[j] = v*-1
        hq.heapify(num_list)
        answer.append(hq.heappop(num_list))
        print(answer)
    else:
        answer = [0,0]
    return answer

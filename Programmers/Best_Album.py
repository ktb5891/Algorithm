def solution(genres, plays):
    dic = dict()
    sum1 = dict()
    for i in range(len(genres)):
        if (genres[i],plays[i]) in dic.keys():
            dic[(genres[i],plays[i])].append(i)
        else:
            dic[(genres[i],plays[i])] = [i]
        if genres[i] in sum1.keys():
            sum1[genres[i]] += plays[i]
        else:
            sum1[genres[i]] = plays[i]
    dic2 = sorted(dic.keys(),reverse = True)
    sum1 = sorted(sum1.items(),key = lambda item : item[1],reverse = True)
    # print(sum1)
    # print(dic)
    # print(dic2)
    answer = []
    while sum1:
        count = 0
        maxi_sum1 = sum1.pop(0)[0]
        # print('max',maxi_sum1)
        for i in dic2:
            if maxi_sum1 == i[0]:
                answer.append(dic[i])
                count += 1
                if len(dic[i]) == 2:
                    count += 1
            if count == 2:
                break
        # print('sum1',sum1)
        # print('ans',answer)
    answer = sum(answer,[])
    # print(answer)
    return answer
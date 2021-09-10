def solution(n, arr1, arr2):
    answer = []
    make_two1 = [[] for _ in range(n)]
    make_two2 = [[] for _ in range(n)]
    idx = 0
    for i,j in zip(arr1,arr2):
        bin_i = bin(i).replace("0b","")
        bin_j = bin(j).replace("0b","")
        while True:
            if len(bin_i) < n:
                bin_i = '0'+bin_i
                continue
            if len(bin_j) < n:
                bin_j = '0'+bin_j
                continue
            else:
                break
        make_two1[idx].append(bin_i)
        make_two2[idx].append(bin_j)
        idx += 1
    # print(make_two1)
    # print(make_two2)
    ans = []
    for i,j in zip(make_two1,make_two2):
        for k,l in zip(i,j):
            for x,y in zip(k,l):
                if x == '1' or y == '1':
                    ans.append('#')
                else:
                    ans.append(' ')
    for i in range(0,len(ans),n):
        answer.append(''.join(ans[i:n+i]))
        
    return answer
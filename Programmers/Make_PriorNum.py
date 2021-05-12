def solution(nums):
    answer = 0
    pri_num = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                # print(nums[i],nums[j],nums[k])
                pri_num.append(nums[i]+nums[j]+nums[k])
    # print(pri_num)
    div = 2
    num = pri_num.pop()
    pri_num.insert(0,3001)
    while pri_num:
        if num == 3001:
            break
        if num == div:
            answer += 1
            div = 2
            num = pri_num.pop()
        elif num%div == 0:
            div = 2
            num = pri_num.pop()
        else:
            div += 1
    
    return answer
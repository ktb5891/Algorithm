def solution(numbers):
    answer = []
    nums = sorted(numbers)
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            answer.append(nums[i]+nums[j])
    answer = sorted(list(set(answer)))
    return answer
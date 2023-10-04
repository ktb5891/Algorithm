import time

# num = str(input())

# def rev_num (number):
#     rev_num = ''
#     for i in range(len(number)):
#         rev_num = number[i]+rev_num
#     return int(rev_num)


# start = time.perf_counter_ns()

# start_num = int(int(num)*(1/2))

# poss_num = set()
# for i in range(int(num)+1,start_num,-1):
#     # print(i, ' // ',rev_num(str(i)))
#     # print(i)
#     if i+rev_num(str(i)) == int(num):
#         poss_num.add(str(i))
#         if rev_num(str(i))+rev_num(str(rev_num(str(i)))) == int(num):
#             poss_num.add(str(rev_num(str(i))))
#         break
#     else:
#         pass

# # print(sorted(list(map(int,list(poss_num)))))
# print(' '.join(list(poss_num)))

# end = time.perf_counter_ns()
# print('코드 실행 시간: %20dns' % (end - start))

def add_reverse(N):
    start = time.perf_counter_ns()
    def reverse_number(number):
        return int(str(number)[::-1])

    N_int = int(N)
    rev_N = reverse_number(N_int)
    max_X = -1

    # Iterate over all possible X values and find the largest one that satisfies the condition
    for X in range(N_int + 1):
        if X + reverse_number(X) == N_int:
            max_X = max(max_X, X)

    if max_X >= 0:
        end = time.perf_counter_ns()
        return print(str(max_X), '코드 실행 시간 : %20dns' % (end - start))
    else:
        end = time.perf_counter_ns()
        return print("", '코드 실행 시간 : %20dns' % (end - start))

# Test cases
print(add_reverse("88"))  # Output: "44"
print(add_reverse("11"))  # Output: "10"
print(add_reverse("121")) # Output: "110"
print(add_reverse("1000"))  # Output: ""
# print(add_reverse("10485827274850"))  # Output: "7382858692013"
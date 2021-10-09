# n = int(input())
# a = list(map(int, input().split()))
# a.sort()

# def binary_search(num):
#     start = 0
#     end = n-1
#     while start <= end :
#         target = (start+end)//2
#         if a[target] == num :
#             return 1
#         elif a[target] > num :
#             end = target - 1
            
#         else:
#             start = target + 1
            
#     return 0

input()
m_list = list(map(int, input().split()))
for num in m_list:
    print(binary_search(num), end = ' ')
input()
n = set(map(int, input().split()))
print(n)
input()
m = list(map(int, input().split()))
for i in m:
    if i in n:
        print(1, end=' ')
    else:
        print(0, end=' ')


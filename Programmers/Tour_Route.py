# def solution(tickets):
#     answer = ["ICN"]
#     tk = sorted(tickets)
#     count = 0
#     while tk:
#         ticket = tk.pop(0)
#         if ticket[0] == answer[-1]:
#             count = 0
#             answer.append(ticket[1])
#         else:
#             count += 1
#             tk.append(ticket)
#         if count > len(tk):
#             recycle = []
#             count = 0
#             recycle.append(answer[-2])
#             recycle.append(answer.pop())
#             tk.append(recycle)
#     return answer

from collections import defaultdict

def solution(tickets):
    answer = []
    adj = defaultdict(list)

    for ticket in tickets:
        adj[ticket[0]].append(ticket[1])

    for key in adj.keys():
        adj[key].sort(reverse=True)

    q = ['ICN']
    while q:
        tmp = q[-1]

        if not adj[tmp]:
            answer.append(q.pop())
        else:
            q.append(adj[tmp].pop())
    answer.reverse()
    return answer
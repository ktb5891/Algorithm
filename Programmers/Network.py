def solution(n, computers):
    answer = 0
    net = {h:[] for h in range(n)}
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                net[i].append(j)
    start = 0
    def bfs(net,start):
        visit = []
        queue = []
        
        queue.append(start)
        
        while queue:
            node = queue.pop(0)
            if node not in visit:
                visit.append(node)
                queue.extend(net[node])
        return visit
    # print(bfs(net,start))
    # print(net)
    net_list = []
    for i in range(n):
        if sorted(bfs(net,i)) not in net_list:
            net_list.append(sorted(bfs(net,i)))
    # print(net_list)
    answer = len(net_list)
    return answer
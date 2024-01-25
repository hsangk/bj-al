from collections import deque

def solution(n, costs):
    answer = 0

    graph = {}
    for i in range(0,n):
        graph[i] = []
    print(graph)
    costs = sorted(costs, key = lambda x : x[-1])
    #print(costs)

    
    for i in costs:
        # print(i)
        if not(graph[i[0]] and graph[i[1]]):
            answer += i[2]
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        else:
            continue
        # print(graph)

    def CheckComplete(target):
        visited = [False]*n
        queue = deque(target[0])
        visited[0] = True
        print(queue)
        while queue:
            v = queue.popleft()
            print(target[v])
            visited[v] = True
            for i in target[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return visited

    ls = CheckComplete(graph)
    print(ls)
    while not all(ls):
        for i in costs:
            print(i)
            if ls[i[0]] != ls[i[1]]:
                answer += i[2]
                graph[i[0]].append(i[1])
                graph[i[1]].append(i[0])
                break        
        ls = CheckComplete(graph)


    return answer
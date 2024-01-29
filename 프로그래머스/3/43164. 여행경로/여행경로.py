

def solution(tickets):
    graph = {}
    for ticket in tickets:
        if ticket[0] in graph:
            graph[ticket[0]].append(ticket[1])
        else:
            graph[ticket[0]] = [ticket[1]]
    print(graph)
    
    for key in graph.keys():
        graph[key].sort(reverse=True)
    
    answer = []
    q = ["ICN"]
    
    while q:
        top = q[-1]
        print(q)
        print('top', top)
        print('grap', graph)
        if top not in graph or len(graph[top]) == 0:
            answer.append(q.pop())
        else:
            next_dest = graph[top].pop()
            q.append(next_dest)
    print(answer)
    return answer[::-1]


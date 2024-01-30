from collections import deque, defaultdict

def solution(n, edge):
    def bfs(start, graph):
        visited = [-1] * (n + 1)
        visited[start] = 0
        # print(visited)
        q = deque([start])
        
        while q:
            node = q.popleft()
            # print(graph[node])
            for neighbor in graph[node]:
                # print(neighbor)
                if visited[neighbor] == -1:
                    visited[neighbor] = visited[node] + 1
                    q.append(neighbor)
        
        return visited
    
    graph = defaultdict(list)
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    distances = bfs(1, graph)
    
    max_distance = max(distances)
    
    answer = distances.count(max_distance)
    
    return answer
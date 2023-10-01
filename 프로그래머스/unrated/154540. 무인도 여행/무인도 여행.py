from collections import deque

def solution(maps):
    answer = []
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    def bfs(x, y):
        visited[x][y] = True
        island_size = int(maps[x][y])
        queue = deque([(x, y)])
        
        while queue:
            cx, cy = queue.popleft()
            
            for m in range(4):
                nx, ny = cx + dx[m], cy + dy[m]
                if 0 <= nx < a and 0 <= ny < b and maps[nx][ny] != "X" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    island_size += int(maps[nx][ny])
                    queue.append((nx, ny))
        
        return island_size
    
    a = len(maps)
    for i in range(a):
        maps[i] = list(maps[i])
    b = len(maps[0])
    visited = [[False] * b for _ in range(a)]
    
    for i in range(a):
        for j in range(b):
            if maps[i][j] != 'X' and not visited[i][j]:
                island_size = bfs(i, j)
                answer.append(island_size)
    
    if not answer:
        answer.append(-1)
    
    answer.sort()
    return answer

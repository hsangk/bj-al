N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    tmp = [[x,y]]
    cnt = 0
    while tmp:
        x, y = tmp.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = graph[x][y] + 1
                tmp.append((nx,ny))

    return graph[-1][-1]


print(bfs(0,0))
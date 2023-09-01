import sys
from collections import deque

n = int(input())
home = [list(map(int, input())) for _ in range(n)]
# home = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, x, y):
    q = deque()
    q.append((x,y))
    graph[x][y]= 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

tmp = []
for i in range(n):
    for j in range(n):
        if home[i][j] == 1:
            tmp.append(bfs(home, i, j))

tmp.sort()
print(len(tmp))
for i in range(len(tmp)):
    print(tmp[i], end='\n')



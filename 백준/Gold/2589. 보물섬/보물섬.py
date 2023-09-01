from collections import deque
import sys
n, m = map(int, input().split())
treasure = []
land = []

for i in range(n):
    tmp = list(map(str, input()))
    for j in range(len(tmp)):
        if tmp[j]=='L':
            land.append((i, j))
    treasure.append(tmp)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(a, b):
    q = deque([[a,b,0]])
    # q.append([[a,b,0]])
    visited[a][b] = True
    while q:
        a, b, distance = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx>= n or ny <0 or ny >= m or visited[nx][ny] or treasure[nx][ny] == 'W':
                continue
            visited[nx][ny]=True
            q.append([nx, ny, distance + 1])
    return distance

max_ = 0
for i in range(len(land)):
    visited = [[False]*m for _ in range(n)]
    distance = bfs(land[i][0], land[i][1])
    if max_ < distance:
        max_ = distance

print(max_)
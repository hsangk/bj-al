from itertools import combinations
from collections import deque

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# BFS를 통해 바이러스가 퍼지는 영역 크기 계산
def bfs():
    q = deque(virus)
    tmp_lab = [row[:] for row in lab]  # deepcopy

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tmp_lab[nx][ny] == 0:
                tmp_lab[nx][ny] = 2
                q.append((nx, ny))

    count = sum(row.count(0) for row in tmp_lab)  # 안전 영역 크기 계산
    return count

# 가능한 모든 벽을 세워보고 최대 안전 영역 크기 찾기
max_safe_area = 0
empty_cells = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
virus = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]

for walls in combinations(empty_cells, 3):
    for x, y in walls:
        lab[x][y] = 1  # 벽 세우기
    max_safe_area = max(max_safe_area, bfs())
    for x, y in walls:
        lab[x][y] = 0  # 벽 다시 없애기

print(max_safe_area)
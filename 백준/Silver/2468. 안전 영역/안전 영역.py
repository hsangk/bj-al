import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
water_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, h):
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        if (0 <= nx < N) and (0 <= ny < N) and not sink_table[nx][ny] and water_board[nx][ny] > h:
            sink_table[nx][ny] = True
            dfs(nx, ny, h)

ans = 1
for k in range(max(map(max, water_board))):
    sink_table = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if water_board[i][j] > k and not sink_table[i][j]:
                count += 1
                sink_table[i][j] = True
                dfs(i, j, k)
    ans = max(ans, count)

print(ans)
import sys
from collections import deque


top, cur, des, up, down = map(int, sys.stdin.readline().split())

tmp = [0] * 1000001
cnt = [0] * 1000001

def bfs(n):
    q = deque([n])
    tmp[n] = 1
    while q:
        v = q.popleft()
        if v == des:
            return cnt[v]

        for nv in (v+up, v-down):
            if 0 < nv <= top and tmp[nv] == 0:
                tmp[nv] = 1
                q.append(nv)
                cnt[nv] = cnt[v] + 1
    if tmp[des]==0:

        return "use the stairs"

print(bfs(cur))

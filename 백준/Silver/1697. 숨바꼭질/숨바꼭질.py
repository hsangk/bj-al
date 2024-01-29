import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
tmp = [0] * 100001

def bfs(x):
    q = deque([x])
    while q:
        a = q.popleft()
        if a == k:
            return tmp[a]
        for na in (a-1,a+1,a*2):
            if 0<= na < 100001 and tmp[na] == 0:
                tmp[na] = tmp[a] + 1
                q.append(na)

print(bfs(n))
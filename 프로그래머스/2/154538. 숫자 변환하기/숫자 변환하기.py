from collections import deque

def solution(x, y, n):
    if x == y:
        return 0

    dis = [-1] * (y + 1)
    q = deque()
    q.append(x)
    dis[x] = 0

    while q:
        nx = q.popleft()
        for i in range(3):
            if i == 0:
                qx = nx * 2
            elif i == 1:
                qx = nx * 3
            else:
                qx = nx + n
            
            if qx <= y and dis[qx] == -1:
                q.append(qx)
                dis[qx] = dis[nx] + 1
                
                if qx == y:
                    return dis[qx]
    
    return -1
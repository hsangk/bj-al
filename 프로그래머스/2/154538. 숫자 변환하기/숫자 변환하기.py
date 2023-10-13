# from collections import deque
# def solution(x, y, n):
#     answer = 0
#     # dis = [0] * (y+1)
#     dis = [0 for _ in range(y+1)]
#     q = deque()
#     q.append(x)
#     # dis[x] = 0
#     if x==y:
#         return 0
#     while q:
#         nx = q.popleft()
#         for i in range(3):
#             if i == 0:
#                 qx = nx * 2
#             elif i == 1:
#                 qx = nx *3
#             else:
#                 qx = nx + n
#             if qx <= y and dis[qx] == 0:
#                 q.append(qx)
#                 dis[qx] = dis[nx] +1
#                 if qx == y:
#                     return dis[qx]
    
#     return -1

def solution(x, y, n):
    if x == y:
        return 0

    dp = [float('inf')] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == float('inf'):
            continue

        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)

        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)

        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    if dp[y] == float('inf'):
        return -1

    return dp[y]

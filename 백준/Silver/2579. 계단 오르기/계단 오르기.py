n = int(input())
stair = [int(input()) for _ in range(n)]
tmp = [0]*n

if len(stair) <= 2:
    print(sum(stair))
else:
    tmp[0] = stair[0]
    tmp[1] = stair[0] + stair[1]
    for i in range(2, n):
        tmp[i] = max(tmp[i-3] + stair[i-1] + stair[i], tmp[i-2] + stair[i])

    print(tmp[-1])
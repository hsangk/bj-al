import heapq
import sys 

n = int(input())
tmp = []
for i in range(n):
    # k = int(input())
    k = int(sys.stdin.readline())
    if k == 0:
        if len(tmp) == 0:
            print(0)
        else:
            print(heapq.heappop(tmp))
    else:
        heapq.heappush(tmp, k)
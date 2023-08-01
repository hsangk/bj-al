from collections import deque
# 리스트 사용시 시간 초과
n = int(input())
tmp = deque([i for i in range(1,n+1)])

while len(tmp)>1:
    tmp.popleft()
    tmp.append(tmp[0])
    tmp.popleft()


print(tmp[0])
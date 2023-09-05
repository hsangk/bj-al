import sys

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    list_ = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    if n>1 :
        list_[0][1] += list_[1][0]
        list_[1][1] += list_[0][0]
    for j in range(2, n):
        list_[0][j] += max(list_[1][j-1], list_[1][j-2])
        list_[1][j] += max(list_[0][j-1], list_[0][j-2])
    print(max(list_[0][n-1], list_[1][n-1]))
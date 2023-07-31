import sys

sys.setrecursionlimit(100001)

n = int(input())
num = []

for i in range(n):
    num.append(i+1)
result_array = sorted(num, reverse=True)
def solve(array):
    print(*array)
    if array == result_array:
        exit()
    for i in range(len(num)-1, 0, -1):
        if array[i-1] < array[i]:
            for j in range(len(num)-1, 0, -1):
                if array[i-1] < array[j]:
                    array[i-1], array[j] = array[j], array[i-1]
                    array = array[:i] + sorted(array[i:])
                    solve(array)

solve(num)
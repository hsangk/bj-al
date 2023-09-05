n = int(input())
list_ = list(map(int, input().split(' ')))

dp = [0] * n

for i in range(1, n):
    list_[i] = max(list_[i], list_[i] + list_[i-1])

print(max(list_))
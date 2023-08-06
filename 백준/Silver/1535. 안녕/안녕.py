import sys

n = int(input())
power_ = sys.stdin.readline().split()
happy_ = sys.stdin.readline().split()

tmp_hap = [0 for i in range(101)]

for i in range(1, n+1):
    L = int(power_[i - 1])
    J = int(happy_[i-1])
    for j in range(100,0,-1):
        if j > L:
            tmp_hap[j] = max(tmp_hap[j], tmp_hap[j-L] + J)

print(tmp_hap[-1])
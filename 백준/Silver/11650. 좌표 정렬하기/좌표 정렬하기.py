n = int(input())
cord = []

for i in range(n):
    a, b = map(int, input().split())
    cord.append([a, b])

cord.sort()
for j in range(len(cord)):
    print(f'{cord[j][0]} {cord[j][1]}')
n = int(input())

def sol(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return sol(x-1) + sol(x-2) + sol(x-3)

tmp = []
for i in range(n):
    k = int(input())
    tmp.append(sol(k))
for j in tmp:
    print(j, end='\n')
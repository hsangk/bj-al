n = int(input())
list = []
for i in range(n):
    list.append(str(input()))

list.sort()
new = []
for i in range(len(list)):
    if list[i] not in new:
        new.append(list[i])
new.sort(key=len)

for j in range(len(new)):
    print(new[j], end='\n')
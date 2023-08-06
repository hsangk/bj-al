n = input()

result = 0
for i in range(0, int(n)):
    sum_ = sum([int(x) for x in str(i)]) + i
    # sum_ = sum((map(int, i)))
    if sum_ == int(n):
        result = i
        break

print(result)
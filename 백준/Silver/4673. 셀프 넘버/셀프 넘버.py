def d(n):
    result = n
    while n > 0:
        result += n % 10
        n //= 10
    return result

self_list = [x for x in range(1, 10001)]
self_list = [True] * 10001

for i in range(1, 10001):
    tmp = d(i)
    if tmp <= 10000:
        self_list[tmp] = False


for i in range(1, 10001):
    if self_list[i]:
        print(i)
def solution(m, n, puddles):
    MOD = 1000000007
    des = [[0] * m for _ in range(n)]

    for b, a in puddles:  # 좌표 a와 b를 바꿈
        des[a - 1][b - 1] = -1

    des[0][0] = 1

    for y in range(n):
        for x in range(m):
            if des[y][x] == -1:
                continue

            if x > 0 and des[y][x - 1] != -1:
                des[y][x] += des[y][x - 1]

            if y > 0 and des[y - 1][x] != -1:
                des[y][x] += des[y - 1][x]

            des[y][x] %= MOD  # 나머지 연산을 각 위치에서 수행

    answer = des[n - 1][m - 1] % MOD
    return answer % MOD
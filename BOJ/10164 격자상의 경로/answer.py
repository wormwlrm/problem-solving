import sys
import math

input = sys.stdin.readline

N, M, K = map(int, input().split())


def get_routes(x, y):
    maps = [[0 for _ in range(y)] for _ in range(x)]

    for i in range(0, x):
        maps[i][0] = 1

    for j in range(0, y):
        maps[0][j] = 1

    for i in range(1, x):
        for j in range(1, y):
            maps[i][j] = maps[i - 1][j] + maps[i][j - 1]

    return maps[x - 1][y - 1]


if K == 0:
    answer = get_routes(N, M)
else:
    x = math.ceil(K / M)
    y = M if (K % M) == 0 else (K % M)

    answer = get_routes(x, y) * get_routes(M - y + 1, N - x + 1)

print(answer)

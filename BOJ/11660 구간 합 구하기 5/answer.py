import sys

input = sys.stdin.readline

N, M = map(int, input().split())

area = []

for _ in range(N):
    area.append(list(map(int, input().split())))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for y in range(1, N + 1):
    for x in range(1, N + 1):
        dp[y][x] = area[y - 1][x - 1] + dp[y][x - 1] + dp[y - 1][x] - dp[y - 1][x - 1]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    if (x1 == x2) and (y1 == y2):
        print(area[y1 - 1][x1 - 1])
    else:
        print(dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 - 1][x1 - 1])

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[0] * (M + 1) for _ in range(N + 1)]

area = []

for _ in range(N):
    area.append(list(map(int, input().split())))

for y in range(1, N + 1):
    for x in range(1, M + 1):
        dp[y][x] = (
            max(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + area[y - 1][x - 1]
        )

print(dp[N][M])

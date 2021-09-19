import sys

input = sys.stdin.readline

N, K = map(int, input().split())

DIVIDE = 10_007

dp = [[1] * (N + 1) for _ in range(N + 1)]

for y in range(1, N + 1):
    for x in range(1, N + 1):
        dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % DIVIDE


print(dp[N - K][K] % DIVIDE)

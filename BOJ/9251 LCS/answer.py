import sys

input = sys.stdin.readline

X = input().strip()
Y = input().strip()

MAXIMUM = 1001

# 가로에 X, 세로에 Y 놓기
dp = [[0] * (len(X) + 1) for _ in range(len(Y) + 1)]

for y in range(1, len(Y) + 1):
    for x in range(1, len(X) + 1):
        ry, rx = y - 1, x - 1

        if X[rx] == Y[ry]:
            dp[y][x] = dp[y - 1][x - 1] + 1
        else:
            dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])

print(max(dp[-1]))

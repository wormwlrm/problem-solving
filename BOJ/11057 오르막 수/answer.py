import sys

input = sys.stdin.readline

DIVIDE = 10007

N = int(input())

# 9 자리 미리 세팅, 제로 패딩
dp = [[0] * 10, [1] * 10] + [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1] for _ in range(1000)]

dp2 = [0] * 1001

for i in range(1, N + 1):
    for j in range(8, -1, -1):
        dp[i][j] = dp[i - 1][j] % DIVIDE + dp[i][j + 1] % DIVIDE

    dp2[i] = sum(dp[i]) % DIVIDE

print(dp2[N])

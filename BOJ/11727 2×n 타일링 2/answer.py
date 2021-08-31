import sys

input = sys.stdin.readline

N = int(input())

DIVIDED = 10_007

dp = [0, 1, 3] + [0] * 1000

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % DIVIDED

print(dp[N])

import sys
import math

input = sys.stdin.readline

dp = [0, 1, 2] + [0] * 1000

divide = 10007

N = int(input())

for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % divide

print(dp[N])

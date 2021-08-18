import sys
import math

input = sys.stdin.readline

N = int(input())

dp = list(range(50001))

# 제곱수
for i in range(2, math.floor(math.sqrt(50001))):
    dp[i ** 2] = 1

    for j in range(i ** 2, 50001):
        dp[j] = min(dp[j], dp[j - i ** 2] + 1)

print(dp[N])

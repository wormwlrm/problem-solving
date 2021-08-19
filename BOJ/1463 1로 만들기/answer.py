import sys
from collections import deque
import math

input = sys.stdin.readline

dp = [float("inf")] * 1000001

N = int(input())

dp[N] = 0


queue = deque([N])

while queue:
    current = queue.popleft()

    if current < 1:
        continue

    if current % 3 == 0 and dp[current] + 1 < dp[current // 3]:
        dp[current // 3] = dp[current] + 1
        queue.append(current // 3)
    if current % 2 == 0 and dp[current] + 1 < dp[current // 2]:
        dp[current // 2] = dp[current] + 1
        queue.append(current // 2)
    if dp[current] + 1 < dp[current - 1]:
        dp[current - 1] = dp[current] + 1
        queue.append(current - 1)

print(dp[1])

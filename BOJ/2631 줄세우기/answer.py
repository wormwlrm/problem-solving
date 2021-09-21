import sys

input = sys.stdin.readline

N = int(input())

children = [0]

dp = [0] * (N + 1)

for _ in range(N):
    children.append(int(input()))

for i in range(1, N + 1):
    current = children[i]

    maximum_index = 0

    for j in range(1, i):
        cursor = children[j]

        if current < cursor:
            continue

        if dp[maximum_index] < dp[j]:
            maximum_index = j

    dp[i] = dp[maximum_index] + 1

LIS = max(dp)

print(N - LIS)

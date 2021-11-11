# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2096%20%EB%82%B4%EB%A0%A4%EA%B0%80%EA%B8%B0

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

numbers = []

max_dp = [[0, 0, 0], [0, 0, 0]]
min_dp = [[0, 0, 0], [0, 0, 0]]

for j in range(N):
    numbers = list(map(int, input().split()))

    if j == 0:
        max_dp[0] = numbers[::]
        min_dp[0] = numbers[::]
        continue

    for i in range(3):
        if i == 0:
            max_dp[1][i] = max(max_dp[0][i], max_dp[0][i + 1]) + numbers[i]
            min_dp[1][i] = min(min_dp[0][i], min_dp[0][i + 1]) + numbers[i]
        elif i == 1:
            max_dp[1][i] = (
                max(max_dp[0][i - 1], max_dp[0][i], max_dp[0][i + 1]) + numbers[i]
            )
            min_dp[1][i] = (
                min(min_dp[0][i - 1], min_dp[0][i], min_dp[0][i + 1]) + numbers[i]
            )
        else:
            max_dp[1][i] = max(max_dp[0][i], max_dp[0][i - 1]) + numbers[i]
            min_dp[1][i] = min(min_dp[0][i], min_dp[0][i - 1]) + numbers[i]

    # 커서(?) 역할 다시 갱신
    max_dp = [max_dp[1][::]] + [[0, 0, 0]]
    min_dp = [min_dp[1][::]] + [[0, 0, 0]]

print(max(max_dp[0]), min(min_dp[0]))

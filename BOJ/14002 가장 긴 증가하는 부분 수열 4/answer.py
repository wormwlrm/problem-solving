# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/14002%20%EA%B0%80%EC%9E%A5%20%EA%B8%B4%20%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4%204

import sys

input = lambda: sys.stdin.readline().rstrip()

dp = [0] * 1_001

N = int(input())

arr = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    maximum = -float("inf")

    for j in range(i):
        if arr[j] < arr[i]:
            maximum = max(maximum, dp[j])

    dp[i] = maximum + 1

maximum = max(dp)
print(maximum)

order = []

for i in range(N, 0, -1):
    if dp[i] == maximum:
        order.append(arr[i])
        maximum -= 1
order.reverse()
print(*order)

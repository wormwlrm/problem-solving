import sys

input = sys.stdin.readline

N = int(input())

steps = list(map(int, input().split()))

dp = [1]

for index in range(1, N):
    dp.append(min(dp[index - 1] + 1, steps[index]))

print(max(dp))

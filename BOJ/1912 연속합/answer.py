import sys

input = sys.stdin.readline

N = int(input())

numbers = [*map(int, input().rstrip().split())]

dp = [0] * N
dp[0] = numbers[0]


for i in range(1, N):
    maximum = max(dp[i - 1] + numbers[i], numbers[i])
    dp[i] = maximum

print(max(dp))

import sys

input = sys.stdin.readline

count = int(input().rstrip())

N = 11

dp = [0, 1, 2, 4]

for i in range(4, N + 1):
    prev1 = dp[i - 1]
    prev2 = dp[i - 2]
    prev3 = dp[i - 3]

    dp.append(prev1 + prev2 + prev3)

for i in range(count):
    current = int(input().rstrip())

    print(dp[current])
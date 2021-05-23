import sys

input = sys.stdin.readline

dp = [(1, 0), (0, 1)]

N = 40

count = int(input().rstrip())

for i in range(N + 1):
    if (i == 0) or (i == 1):
        continue
    
    prev1 = i - 2
    prev2 = i - 1

    current = (dp[prev1][0] + dp[prev1][1], dp[prev2][0] + dp[prev2][1])

    dp.append(current)

for i in range(count):
    current = int(input().rstrip())

    print(dp[current][0], dp[current][1], sep=" ")
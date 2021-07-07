import sys

input = sys.stdin.readline

count = int(input())

dp = [1, 1]

if (count == 0) or (count == 1):
    print(dp[count])
else:
    while (count > len(dp)):
        dp.append(dp[-1] + dp[-2])

    print(dp[-1])

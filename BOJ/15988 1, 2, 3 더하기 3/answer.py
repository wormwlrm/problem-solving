import sys

input = sys.stdin.readline

count = int(input())

divided = 1000000009

# zero-padding
dp = [0, 1, 2, 4]

for _ in range(1000000):
    dp3 = dp[-3]
    dp2 = dp[-2]
    dp1 = dp[-1]
    dp.append((dp3 + dp2 + dp1) % divided)

for _ in range(count):
    print(dp[int(input())])

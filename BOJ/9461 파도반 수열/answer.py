import sys

input = sys.stdin.readline

T = int(input())

dp = [0, 1, 1, 1, 2, 2, 3]

for i in range(7, 101):
    dp.append(dp[i - 1] + dp[i - 5])

# 육각형 모양으로 회전
for _ in range(T):
    print(dp[int(input())])

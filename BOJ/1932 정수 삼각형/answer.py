import sys

input = sys.stdin.readline

N = int(input())

triangle = []

for _ in range(N):
    triangle.append(list(map(int, input().split())))

dp = [[0 for _ in range(i + 1)] for i in range(N)]

dp[0][0] = triangle[0][0]

if (N) == 1:
    print(dp[0][0])
    exit()

dp[1][0] = dp[0][0] + triangle[1][0]
dp[1][1] = dp[0][0] + triangle[1][1]

for i in range(2, N):
    temp = []

    # 각 숫자
    for j in range(len(dp[i - 1])):
        current = dp[i - 1][j]

        for k in range(2):
            dp[i][j + k] = max(dp[i][j + k], current + triangle[i][j + k])

print(max(dp[-1]))

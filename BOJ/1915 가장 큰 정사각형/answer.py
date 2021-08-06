import sys

input = sys.stdin.readline

# 가로, 세로
N, M = map(int, input().split())

area = []

dp = []

for _ in range(N):
    area.append(list(map(int, list(input().rstrip()))))
    dp.append([0 for _ in range(M)])


def get_dp(i, j):
    # 첫 번째 줄에 있는 경우는 area 그대로 리턴
    if i == 0 or j == 0:
        return area[j][i]

    up = dp[j - 1][i]
    left_up = dp[j - 1][i - 1]
    left = dp[j][i - 1]

    return min(up, left_up, left) + 1


maximum = 0

# 세로
for j in range(N):
    # 가로
    for i in range(M):
        if area[j][i] == 1:
            dp[j][i] = 1

        if dp[j][i] == 0:
            continue

        current = get_dp(i, j)

        dp[j][i] = current
        maximum = max(maximum, current)

print(maximum ** 2)

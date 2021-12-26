# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/17404%20RGB%EA%B1%B0%EB%A6%AC%202

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

rgb = [[0, 0, 0] for _ in range(N)]

# rgb 채우기
for i in range(N):
    rgb[i] = list(map(int, input().split()))

# 첫 집의 색을 i로 정했을 때의 DP
dp = [[float("inf"), float("inf"), float("inf")] for _ in range(3)]

answer = float("inf")


# 첫 집의 색을 정하고 시작해보자
for i in range(3):
    for j in range(3):
        if i == j:
            dp[i][j] = rgb[0][j]
        else:
            dp[i][j] = float("inf")

    for j in range(1, N):
        red, green, blue = rgb[j]
        current_dp = dp[i]
        temp = [0, 0, 0]

        temp[0] = min(current_dp[1], current_dp[2]) + red
        temp[1] = min(current_dp[0], current_dp[2]) + green
        temp[2] = min(current_dp[0], current_dp[1]) + blue

        dp[i] = temp

    # 마지막 줄은 같은 1번쨰에서 선택한 거 아닌 거만
    for j in range(3):
        if i == j:
            continue
        answer = min(answer, dp[i][j])

print(answer)

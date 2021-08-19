import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

last = numbers[-1]

numbers = numbers[:-1:]

dp = [[0] * 21 for _ in range(N - 1)]

dp[0][numbers[0]] = 1

# 턴
for i in range(N - 2):
    # 숫자
    for j in range(21):
        if dp[i][j] == 0:
            continue

        # 다음 숫자 더한 거
        added = j + numbers[i + 1]
        if added <= 20:
            dp[i + 1][added] = dp[i][j] + dp[i + 1][added]

        # 뺀 거
        subtracted = j - numbers[i + 1]
        if subtracted >= 0:
            dp[i + 1][subtracted] = dp[i][j] + dp[i + 1][subtracted]

print(dp[-1][last])

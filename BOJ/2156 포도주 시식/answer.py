import sys

input = sys.stdin.readline

N = int(input())

cup = [0]

dp = [0] * (N + 1)

if N == 1:
    print(int(input()))
    exit()

for _ in range(N):
    cup.append(int(input()))

dp[1] = cup[1]
dp[2] = cup[1] + cup[2]

for i in range(3, N + 1):
    dp[i] = max(
        # 그 전 거를 그대로 가져오던지
        dp[i - 1],
        # 두 칸 빼고 새로 한 잔 먹던지
        dp[i - 2] + cup[i],
        # 세 칸 빼고 두잔 새로 먹던지
        dp[i - 3] + cup[i - 1] + cup[i],
    )

print(max(dp))

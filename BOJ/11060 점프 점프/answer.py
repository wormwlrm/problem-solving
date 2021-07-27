import sys
from math import isinf

input = sys.stdin.readline

N = int(input())

MAXIMUM = 1001

# 인덱스만큼의 거리까지 가는데 걸리는 횟수
dp = [float("inf")] * MAXIMUM
dp[0] = 0

numbers = list(map(int, input().split()))

for index in range(N):
    current = numbers[index]

    if current == 0:
        continue

    for i in range(1, current + 1):
        # 오버플로 ㄴㄴ
        if index + i > MAXIMUM - 1:
            continue

        # 횟수 한 번 추가한 걸로 갱신
        dp[index + i] = min(dp[index + i], 1 + dp[index])

if isinf(dp[N - 1]):
    print(-1)
else:
    print(dp[N - 1])

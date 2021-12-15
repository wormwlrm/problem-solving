# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2624%20%EB%8F%99%EC%A0%84%20%EB%B0%94%EA%BF%94%EC%A3%BC%EA%B8%B0

import sys

input = lambda: sys.stdin.readline().rstrip()

# 지폐
T = int(input())

# 갯수
k = int(input())

money = [list(map(int, input().split())) for _ in range(k)]

money.sort(reverse=True)
dp = (T + 1) * [0]
dp[0] = 1

for coin_value, coin_count in money:
    for current_money in range(T, 1, -1):
        for current_count in range(1, coin_count + 1):
            if current_money - current_count * coin_value >= 0:
                dp[current_money] += dp[current_money - current_count * coin_value]
print(dp[T])

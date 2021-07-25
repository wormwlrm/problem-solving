import sys
from math import isinf

input = sys.stdin.readline

N, K = map(int, input().split())

coins = set([])

for _ in range(N):
    coins.add(int(input()))

coins = sorted(list(coins))

MAX_COUNT = 10000

MAX_COST = 100000

dp = [0] + [float("inf")] * MAX_COUNT

for coin in coins:
    for i in range(coin, K + 1):
        # 현재 코인만큼 가치를 빼고, 1을 더해서 코인을 추가하겠다는 뜻!
        dp[i] = min(dp[i], dp[i - coin] + 1)

if (isinf(dp[K])):
    print(-1)
else:
    print(dp[K])
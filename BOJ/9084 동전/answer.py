import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())

    coins = list(map(int, input().split()))

    M = int(input())

    # dp[0]을 초기화
    dp = [1] + [0 for _ in range(M)]

    for coin_index in range(N):
        for weight in range(coins[coin_index], M + 1):
            dp[weight] = dp[weight] + dp[weight - coins[coin_index]]

    print(dp[-1])

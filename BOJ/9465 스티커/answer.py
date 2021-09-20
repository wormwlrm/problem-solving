import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())
    cards = []

    for _ in range(2):
        cards.append(list(map(int, input().split())))

    maximum = 0
    dp = [[0] * (N) for _ in range(2)]

    # 0번째 인덱스 초기화
    dp[0][0] = cards[0][0]
    dp[1][0] = cards[1][0]

    if N >= 2:
        # 1번째 인덱스 초기화
        dp[0][1] = cards[1][0] + cards[0][1]
        dp[1][1] = cards[0][0] + cards[1][1]

    if N >= 3:
        for i in range(2, N):
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + cards[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + cards[1][i]

    print(max(dp[0][N - 1], dp[1][N - 1]))

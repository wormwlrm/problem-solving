# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/4485%20%EB%85%B9%EC%83%89%20%EC%98%B7%20%EC%9E%85%EC%9D%80%20%EC%95%A0%EA%B0%80%20%EC%A0%A4%EB%8B%A4%EC%A7%80?

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

count = 1

while True:
    N = int(input())

    if N == 0:
        break

    area = []

    for _ in range(N):
        area.append(list(map(int, input().split())))

    # 특정 칸까지 가는데 비용이 얼마나 걸리는지
    dp = [[float("inf") for _ in range(N)] for _ in range(N)]
    dp[0][0] = area[0][0]

    queue = [(dp[0][0], 0, 0)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        cost, cy, cx = current = heapq.heappop(queue)

        if (cy, cx) == (N - 1, N - 1):
            break

        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < N and 0 <= nx < N:
                if dp[ny][nx] > dp[cy][cx] + area[ny][nx]:
                    dp[ny][nx] = dp[cy][cx] + area[ny][nx]
                    heapq.heappush(queue, (dp[cy][cx] + area[ny][nx], ny, nx))
    print("Problem {}: {}".format(count, dp[N - 1][N - 1]))
    count += 1

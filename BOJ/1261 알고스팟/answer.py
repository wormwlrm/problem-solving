# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1261%20%EC%95%8C%EA%B3%A0%EC%8A%A4%ED%8C%9F

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

# 가로, 세로
N, M = map(int, input().split())

area = []

for _ in range(M):
    area.append(list(map(int, list(input()))))

dp = [[float("inf")] * (N) for _ in range(M)]
dp[0][0] = 0

queue = deque([(0, 0, 0)])

while queue:
    x, y, broken = current = queue.popleft()

    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            # 노코스트로 이동 가능
            if area[ny][nx] == 0:
                # 갱신 가능할 때만 큐에 넣기
                if broken < dp[ny][nx]:
                    dp[ny][nx] = broken
                    queue.append((nx, ny, broken))
            # 벽 부셔야 이동 가능
            else:
                # 갱신 가능할 때만 큐에 넣기
                if broken + 1 < dp[ny][nx]:
                    dp[ny][nx] = broken + 1
                    queue.append((nx, ny, broken + 1))

print(dp[M - 1][N - 1])

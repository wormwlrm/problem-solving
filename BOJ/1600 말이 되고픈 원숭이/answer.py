# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1600%20%EB%A7%90%EC%9D%B4%20%EB%90%98%EA%B3%A0%ED%94%88%20%EC%9B%90%EC%88%AD%EC%9D%B4

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

K = int(input())

W, H = map(int, input().split())

# 3차원 배열, K는 말뜀박질 횟수
dp = [[[float("inf")] * (W) for _ in range(H)] for _ in range(K + 1)]
dp[0][0][0] = 0

visited = {}

area = []

for r in range(H):
    line = list(map(int, input().split()))
    area.append(line)


horse_direction = [
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
]
direction = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


def bfs():
    queue = deque([(0, 0, 0)])
    depth = -1

    while queue:
        depth += 1

        for _ in range(len(queue)):
            k, y, x = current = queue.popleft()

            if y == H - 1 and x == W - 1:
                return depth

            # 뜀박질 가능
            if k < K:
                for dy, dx in horse_direction:
                    ny, nx = y + dy, x + dx

                    # 이동 가능하며
                    if (0 <= ny < H) and (0 <= nx < W) and area[ny][nx] == 0:
                        # 갱신 가치가 있고 방문 안한 것인지
                        if (
                            dp[k][ny][nx] > dp[k][y][x] + 1
                            and (k + 1, ny, nx) not in visited
                        ):
                            visited[(k + 1, ny, nx)] = True
                            dp[k + 1][ny][nx] = min(dp[k + 1][ny][nx], dp[k][y][x] + 1)
                            queue.append((k + 1, ny, nx))

            # 뜀박질 안하는 경우
            for dy, dx in direction:
                ny, nx = y + dy, x + dx

                # 이동 가능하며
                if (0 <= ny < H) and (0 <= nx < W) and area[ny][nx] == 0:
                    # 갱신 가치가 있고 방문 안한 것인지
                    if dp[k][ny][nx] > dp[k][y][x] + 1 and (k, ny, nx) not in visited:
                        visited[(k, ny, nx)] = True
                        dp[k][ny][nx] = dp[k][y][x] + 1
                        queue.append((k, ny, nx))
    return -1


print(bfs())

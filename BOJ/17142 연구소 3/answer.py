# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/17142%20%EC%97%B0%EA%B5%AC%EC%86%8C%203

import sys
from collections import deque
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

area = []

walls = []

empty = []

deactivated_virus = []

for y in range(N):
    line = list(map(int, input().split()))

    for x, value in enumerate(range(N)):
        if line[value] == 0:
            empty.append((y, x))
        elif line[value] == 2:
            deactivated_virus.append((y, x))
        elif line[value] == 1:
            walls.append((y, x))

    area.append(line)


def bfs(virus: list):
    visited = [[float("inf")] * N for _ in range(N)]

    empty_counter = len(empty)

    for vy, vx in virus:
        visited[vy][vx] = 0

    for wy, wx in walls:
        visited[wy][wx] = -1

    queue = deque(virus)
    depth = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue and empty_counter > 0:
        depth += 1

        for _ in range(len(queue)):
            y, x = queue.popleft()

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                # 맵 안에 있으면서
                if 0 <= ny < N and 0 <= nx < N:
                    # 0인 경우
                    if area[ny][nx] == 0 and visited[ny][nx] == float("inf"):
                        visited[ny][nx] = depth
                        queue.append((ny, nx))
                        empty_counter -= 1

                    # 2인 경우
                    elif area[ny][nx] == 2 and visited[ny][nx] == float("inf"):
                        should_be_counted = False

                        # 해당 칸의 4방향을 다시 둘러보자
                        for ddy, ddx in directions:
                            nny, nnx = ny + ddy, nx + ddx

                            if 0 <= nny < N and 0 <= nnx < N:
                                # 빈칸이거나 또 바이러스 있는 경우만 유망함
                                if area[nny][nnx] in [0, 2] and visited[nny][
                                    nnx
                                ] == float("inf"):
                                    should_be_counted = True
                                    break

                        if should_be_counted:
                            visited[ny][nx] = depth
                            queue.append((ny, nx))

    for y in range(N):
        for x in range(N):
            # 비활성 바이러스가 아니고 방문 못한다면
            if area[y][x] != 2 and visited[y][x] == float("inf"):
                return float("inf")

    return depth


if len(empty) == 0:
    print(0)
    exit()

combos = list(combinations(deactivated_virus, M))

answer = float("inf")

for combo in combos:
    answer = min(answer, bfs(combo))

print(answer if answer != float("inf") else -1)

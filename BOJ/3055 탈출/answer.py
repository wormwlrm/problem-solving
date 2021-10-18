# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/3055%20%ED%83%88%EC%B6%9C

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())

area = []

beaver = []

water = []

for h in range(H):
    line = list(input())

    for w, item in enumerate(line):
        if item == "S":
            beaver.append((h, w, "S"))
        elif item == "*":
            water.append((h, w, "*"))

    area.append(line)

visited = [[float("inf")] * W for _ in range(H)]


def bfs():
    queue = deque(water + beaver)

    for h1, w1, _type in water + beaver:
        visited[h1][w1] = 0

    turn = 0

    while queue:
        turn += 1

        for _ in range(len(queue)):
            cy, cx, type = queue.popleft()
            current = area[cy][cx]

            # 비버의 경우
            if type == "S" and current == "D":
                return visited[cy][cx]

            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = cy + dy, cx + dx

                # 벽은 가지 않게
                if 0 <= ny < H and 0 <= nx < W and area[ny][nx] != "X":

                    # 만약 물이면 비버 지나가던 말던 그냥 물로 덮어씌우기
                    if type == "*":
                        # 이미 물로 차있으면 패스
                        if visited[ny][nx] < 0:
                            continue
                        # 도착점은 침범 못함
                        if area[ny][nx] == "D":
                            continue

                        # 물 아니라 비버 이동 경로면 덮어씌우기
                        visited[ny][nx] = -turn
                        queue.append((ny, nx, type))

                    # 비버면
                    else:
                        # 물이면 패쓰
                        if visited[ny][nx] < 0:
                            continue
                        # 이미 방문한 칸도 패쓰
                        if 0 < visited[ny][nx] < float("inf"):
                            continue

                        visited[ny][nx] = turn
                        queue.append((ny, nx, type))

    return "KAKTUS"


print(bfs())

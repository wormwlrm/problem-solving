import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

# 전역변수 초기화
L = R = C = 0


def is_valid_child(graph, dz, dy, dx):
    # 영역 탈출
    if (dx < 0) or (dy < 0) or (dz < 0) or L <= dz or R <= dy or C <= dx:
        return False

    # 벽
    elif graph[dz][dy][dx] == "#":
        return False

    return True


def get_children(graph, oz, oy, ox):
    children = []

    directions = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    for direction in directions:
        dz = direction[0] + oz
        dy = direction[1] + oy
        dx = direction[2] + ox

        if is_valid_child(graph, dz, dy, dx):
            children.append((dz, dy, dx))

    return children


def bfs(graph, sz, sy, sx):
    queue = deque([(sz, sy, sx)])

    visited = [[[False] * (C) for _ in range(R)] for _ in range(L)]

    turn = -1

    while queue:
        turn += 1

        for _ in range(len(queue)):
            cz, cy, cx = current = queue.popleft()

            if graph[cz][cy][cx] == "E":
                return turn

            children = get_children(graph, cz, cy, cx)

            for child in children:
                chz, chy, chx = child

                if not visited[chz][chy][chx]:
                    queue.append(child)
                    visited[chz][chy][chx] = True

    return -1


while True:
    # 층, 세로, 가로
    L, R, C = map(int, input().split())

    if [L, R, C] == [0, 0, 0]:
        break

    sz, sy, sx = 0, 0, 0

    area = []

    for f in range(L):
        floor = []

        for r in range(R):
            row = list(input())

            for c in range(C):
                if row[c] == "S":
                    sz, sy, sx = f, r, c

            floor.append(row)

        area.append(floor)

        dummy = input()

    turn = bfs(area, sz, sy, sx)

    if turn == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {turn} minute(s).")

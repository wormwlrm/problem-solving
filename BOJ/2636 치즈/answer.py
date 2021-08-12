import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())


cheese = [list(map(int, input().split())) for _ in range(H)]


def doing(state):
    for i in range(H):
        for j in range(W):
            if state[i][j] == 1:
                return True
    return False


def is_valid_child(graph, dx, dy, x, y):
    if (dx < 0) or (dy < 0) or W <= dx or H <= dy:
        return False
    # 현재값이 1이면 공기와 맞닿은 치즈임,
    # 더 이상 탐색하지 않음
    elif graph[y][x] == 1:
        return False
    return True


def get_children(graph, x, y):
    # 상, 하, 좌, 우
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    children = []

    for direction in directions:
        dx = direction[0] + x
        dy = direction[1] + y

        if is_valid_child(graph, dx, dy, x, y):
            children.append((dx, dy))

    return children


def dfs(graph, x, y):
    queue = deque([(x, y)])

    visited = [[0] * (W) for _ in range(H)]
    visited[y][x] = 1

    melt = []

    while queue:
        cx, cy = queue.popleft()

        if graph[cy][cx] == 1:
            melt.append((cx, cy))
            continue

        children = get_children(graph, cx, cy)

        for child in children:
            chx, chy = child

            if visited[chy][chx] == 0:
                queue.append(child)
                visited[chy][chx] = 1

    return melt


turn = 0
melting_count = 0

while doing(cheese):
    melting_cheese = dfs(cheese, 0, 0)
    melting_count = len(melting_cheese)

    # 치즈 녹이기
    for x, y in melting_cheese:
        cheese[y][x] = 0

    turn += 1

print(turn)
print(melting_count)

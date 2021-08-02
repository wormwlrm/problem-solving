import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def get_children(X, Y, M, N, maps):
    children = []

    # 상
    if Y - 1 >= 0 and maps[Y - 1][X] == 1:
        children.append((X, Y - 1))
    # 하
    if Y + 1 <= N - 1 and maps[Y + 1][X] == 1:
        children.append((X, Y + 1))
    # 좌
    if X - 1 >= 0 and maps[Y][X - 1] == 1:
        children.append((X - 1, Y))
    # 우
    if X + 1 <= M - 1 and maps[Y][X + 1] == 1:
        children.append((X + 1, Y))

    return children


def dfs(N, M, Y, X, maps, visited):
    queue = deque([])
    queue.append((X, Y))
    group = 0

    while queue:
        cX, cY = queue.popleft()

        # 방문한 부분
        if visited[cY][cX] == 1:
            continue
        # 배추 없는 부분
        elif maps[cY][cX] == 0:
            visited[cY][cX] = 1
            continue

        visited[cY][cX] = 1

        children = get_children(cX, cY, M, N, maps)
        group = 1

        for x, y in children:
            if visited[y][x] == 0:
                queue.append((x, y))

    return group


for _ in range(T):
    M, N, K = map(int, input().split())

    maps = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for k in range(K):
        X, Y = map(int, input().split())

        maps[Y][X] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            count += dfs(N, M, i, j, maps, visited)
    print(count)

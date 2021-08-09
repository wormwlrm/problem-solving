import sys
from collections import deque

input = sys.stdin.readline

# N이 세로, M이 가로
N, M = map(int, (input().split()))

before = []

after = []

for n in range(N):
    before.append(list(map(int, input().split())))

for n in range(N):
    after.append(list(map(int, input().split())))


def get_children(x, y, visited, target):
    children = []

    # 상
    if (y - 1 >= 0) and before[y - 1][x] == target and visited[y - 1][x] == 0:
        children.append((x, y - 1))
    # 하
    if (y + 1 < N) and before[y + 1][x] == target and visited[y + 1][x] == 0:
        children.append((x, y + 1))
    # 좌
    if (x - 1 >= 0) and before[y][x - 1] == target and visited[y][x - 1] == 0:
        children.append((x - 1, y))
    # 우
    if (x + 1 < M) and before[y][x + 1] == target and visited[y][x + 1] == 0:
        children.append((x + 1, y))

    return children


def dfs(x, y):
    queue = deque([(x, y)])

    visited = [[0 for _ in range(M)] for _ in range(N)]

    target = before[y][x]
    to = after[y][x]

    while queue:
        cx, cy = queue.popleft()

        # 방문한 경우
        if visited[cy][cx] == 1:
            continue

        visited[cy][cx] = 1
        before[cy][cx] = to

        children = get_children(cx, cy, visited, target)

        for child in children:
            chx, chy = child
            if visited[chy][chx] == 0:
                queue.append((chx, chy))


visited = [[0 for _ in range(M)] for _ in range(N)]


def traversal():
    for i in range(N):
        for j in range(M):
            if before[i][j] != after[i][j]:
                return dfs(j, i)


traversal()


def is_answer():
    for i in range(N):
        for j in range(M):
            if before[i][j] != after[i][j]:
                return False
    return True


if is_answer():
    print("YES")
else:
    print("NO")

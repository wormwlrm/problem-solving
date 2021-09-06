import sys
from collections import deque

input = sys.stdin.readline

# 세로 가로 영역
M, N, K = map(int, input().split())

area = [[0 for _ in range(N)] for _ in range(M)]

visited = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())

    for ty in range(ry - ly):
        for tx in range(rx - lx):
            area[ly + ty][lx + tx] += 1


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_valid_child(dy, dx):
    # 영역 탈출
    if (dx < 0) or (dy < 0) or N <= dx or M <= dy:
        return False
    # 벽
    elif area[dy][dx] >= 1:
        return False

    return True


def get_children(oy, ox):
    children = []

    for direction in directions:
        dy = direction[0] + oy
        dx = direction[1] + ox

        if is_valid_child(dy, dx):
            children.append((dy, dx))

    return children


def dfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 1
    group = []

    while queue:
        current = queue.popleft()
        cy, cx = current

        group.append(current)

        children = get_children(cy, cx)

        for child in children:
            chy, chx = child
            if visited[chy][chx] == 0:
                visited[chy][chx] = 1
                queue.append(child)

    return group


groups = []

for ay in range(M):
    for ax in range(N):
        if visited[ay][ax] == 1:
            continue
        if area[ay][ax] >= 1:
            visited[ay][ax] = 1
            continue

        group = dfs(ay, ax)
        groups.append(group)

groups.sort(key=lambda group: len(group))

lengths = []

for group in groups:
    lengths.append(len(group))

print(len(groups))
print(*lengths)

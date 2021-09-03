import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

area = [list(map(int, list(input().strip()))) for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]

groups = []

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_valid_child(dy, dx):
    # 영역 탈출
    if (dx < 0) or (dy < 0) or N <= dx or N <= dy:
        return False
    # 벽
    elif area[dy][dx] == 0:
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
    visited[y][x] = True
    group = []

    while queue:
        current = queue.popleft()
        cy, cx = current

        children = get_children(cy, cx)
        group.append(current)

        for child in children:
            chy, chx = child
            if visited[chy][chx] == False:
                queue.append(child)
                visited[chy][chx] = True

    return group


for y in range(N):
    for x in range(N):
        if visited[y][x] == True:
            continue

        if area[y][x] == 0:
            visited[y][x] = True
            continue

        group = dfs(y, x)

        if len(group) >= 1:
            groups.append(group)

print(len(groups))

for group in sorted(groups, key=lambda x: len(x)):
    print(len(group))

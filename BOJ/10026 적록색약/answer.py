import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

area = [list(input().strip()) for _ in range(N)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_valid_child(dy, dx, oy, ox, weakness):
    # 영역 탈출
    if (dx < 0) or (dy < 0) or N <= dx or N <= dy:
        return False

    if area[oy][ox] != area[dy][dx]:

        # 색깔 다르긴 한데, 적록 색약 켜져 있는 경우만 예외 처리
        if weakness == True:
            if area[oy][ox] in ["R", "G"] and area[dy][dx] in ["R", "G"]:
                return True

        return False

    return True


def get_children(oy, ox, weakness):
    children = []

    for direction in directions:
        dy = direction[0] + oy
        dx = direction[1] + ox

        if is_valid_child(dy, dx, oy, ox, weakness):
            children.append((dy, dx))

    return children


def dfs(y, x, weakness):
    queue = deque([(y, x)])
    visited[y][x] = True
    group = []

    while queue:
        current = queue.popleft()
        cy, cx = current

        children = get_children(cy, cx, weakness)
        group.append(current)

        for child in children:
            chy, chx = child
            if visited[chy][chx] == False:
                queue.append(child)
                visited[chy][chx] = True

    return group


answer = []

for T in range(2):
    if T == 0:
        weakness = False
    else:
        weakness = True

    visited = [[False for _ in range(N)] for _ in range(N)]
    groups = []

    for y in range(N):
        for x in range(N):
            if visited[y][x] == True:
                continue

            group = dfs(y, x, weakness)

            if len(group) >= 1:
                groups.append(group)

    answer.append(len(groups))

print(*answer)

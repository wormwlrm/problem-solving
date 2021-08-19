import sys
from collections import deque
import math

input = sys.stdin.readline

N, L, R = map(int, input().split())

area = []

for _ in range(N):
    area.append(list(map(int, input().split())))

days = 0

# 상(0), 우(1), 하(2), 좌(3)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 두 점 사이의 문을 열어야 하는지
def should_open(ay, ax, by, bx):
    return L <= abs(area[ay][ax] - area[by][bx]) <= R


def should_continue():
    # 가로 방향 탐색
    for y in range(N):
        for x in range(N - 1):
            if should_open(y, x, y, x + 1):
                return True

    # 세로 방향 탐색
    for y in range(N - 1):
        for x in range(N):
            if should_open(y, x, y + 1, x):
                return True

    return False


def valid(before_y, before_x, after_y, after_x):
    # 경계선 바깥
    if after_y < 0 or after_x < 0 or N - 1 < after_x or N - 1 < after_y:
        return False

    # 국경선 안 열리는 경우
    if not should_open(before_y, before_x, after_y, after_x):
        return False

    return True


def get_children(y, x):
    children = []

    for direction in directions:
        dy, dx = direction

        if valid(y, x, dy + y, dx + x):
            children.append((dy + y, dx + x))

    return children


def bfs(y, x, visited):
    queue = deque([(y, x)])
    visited[y][x] = True

    group = []

    while queue:
        cy, cx = queue.popleft()

        group.append((cy, cx))

        children = get_children(cy, cx)

        for child in children:
            chy, chx = child
            if visited[chy][chx] == False:
                queue.append(child)
                visited[chy][chx] = True

    return group


def flatten(groups):
    for group in groups:
        if len(group) == 1:
            continue

        acc = 0

        for y, x in group:
            acc += area[y][x]

        avg = math.floor(acc / len(group))

        for y, x in group:
            area[y][x] = avg


while should_continue():
    visited = [[False] * N for _ in range(N)]

    groups = []

    for y in range(N):
        for x in range(N):
            if visited[y][x] == True:
                continue

            group = bfs(y, x, visited)
            groups.append(group)

    flatten(groups)
    days += 1

print(days)

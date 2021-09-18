import sys
from copy import deepcopy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

area = []

chickens = []

homes = []


for y in range(N):
    line = list(map(int, input().split()))

    for x, spot in enumerate(line):
        if spot == 2:
            chickens.append((y, x))

            # 치킨집을 일단 지움, 나중에 조합으로 선택해서 넣기 위해
            line[x] = 0

        elif spot == 1:
            homes.append((y, x))

    area.append(line)

combos = list(combinations(chickens, M))


def get_selected_area(combo):
    global area

    current_area = deepcopy(area)

    for y, x in combo:
        current_area[y][x] = 2

    return current_area


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_valid_child(dy, dx):
    # 영역 탈출
    if (dx < 0) or (dy < 0) or N <= dx or N <= dy:
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


def dfs(graph, combo):
    visited = [[False] * N for _ in range(N)]
    queue = deque([])

    for spots in combo:
        sy, sx = spots
        queue.append(spots)
        visited[sy][sx] = True

    depth = -1

    acc = 0

    while queue:
        depth += 1

        for _ in range(len(queue)):
            cy, cx = queue.popleft()

            if graph[cy][cx] == 1:
                acc += depth

            for child in get_children(cy, cx):
                chy, chx = child

                if not visited[chy][chx]:
                    visited[chy][chx] = True
                    queue.append(child)

    return acc


def get_chicken_distance(area, combo):
    distance = 0

    distance += dfs(area, combo)

    return distance


minimum = float("inf")


def get_distance(combo):
    global homes, minimum, area

    selected_area = get_selected_area(combo)
    current_distance = get_chicken_distance(selected_area, combo)

    minimum = min(minimum, current_distance)


for combo in combos:
    get_distance(combo)

print(minimum)

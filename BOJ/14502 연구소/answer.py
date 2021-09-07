import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

area = []

for _ in range(N):
    area.append(list(map(int, input().split())))

# 땅을 일단 저장
ground = []

viruses = []

for y in range(N):
    for x in range(M):
        if area[y][x] == 0:
            ground.append((y, x))
        elif area[y][x] == 2:
            viruses.append((y, x))


combos = list(combinations(ground, 3))


def get_guided_map(area, walls):
    current_area = area

    for wall in walls:
        wy, wx = wall

        current_area[wy][wx] = 1

    return current_area


def is_valid_child(graph, dy, dx):
    # 영역 탈출
    if (dx < 0) or (dy < 0) or M <= dx or N <= dy:
        return False
    # 벽이나 다른 바이러스
    elif graph[dy][dx] in [1, 2]:
        return False
    return True


def get_children(graph, oy, ox):
    children = []

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for direction in directions:
        dy = direction[0] + oy
        dx = direction[1] + ox

        if is_valid_child(graph, dy, dx):
            children.append((dy, dx))

    return children


def bfs(graph, visited, y, x):
    queue = deque([(y, x)])
    visited[y][x] = True
    group = []

    while queue:
        current = queue.popleft()
        cy, cx = current

        group.append(current)

        children = get_children(graph, cy, cx)

        for child in children:
            chy, chx = child
            if visited[chy][chx] == False:
                visited[chy][chx] = True
                queue.append(child)

    return group


def get_viruses_expended_map(area, viruses):
    current_area = area
    visited = [[False for _ in range(M)] for _ in range(N)]

    groups = []

    for virus in viruses:
        vy, vx = virus
        current_area[vy][vx] = 2

    for virus in viruses:
        vy, vx = virus

        group = bfs(current_area, visited, vy, vx)
        groups.append(group)

    for group in groups:
        for gy, gx in group:
            current_area[gy][gx] = 2

    return current_area


def get_count_of_space(area):
    current_area = area
    acc = 0

    for y in range(N):
        for x in range(M):
            if current_area[y][x] == 0:
                acc += 1
    return acc


def is_useless_combo(graph, combos):

    for combo in combos:
        cy, cx = combo

        # 8방향 체크
        directions = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]

        for direction in directions:
            dy = direction[0] + cy
            dx = direction[1] + cx

            if is_valid_child(graph, dy, dx):
                return False

    return True


answer = 0

for combo in combos:
    if is_useless_combo(area, combo):
        continue

    current_area = deepcopy(area)
    guided_map = get_guided_map(current_area, combo)
    expended_map = get_viruses_expended_map(guided_map, viruses)
    answer = max(answer, get_count_of_space(expended_map))

print(answer)

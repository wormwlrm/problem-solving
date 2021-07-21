import sys
from typing import Tuple
from collections import deque


input = sys.stdin.readline

R, C = map(int, input().split())

# 입력 받은 거
field = []
# 그룹 구분 짓는 거
visited = []

for i in range(R):
    row = list(input().rstrip())

    field.append(row)

    visited.append([None for _ in range(C)])


def is_reachable(coord: Tuple[int, int]):
    # 좌표 밖으로 나가는 경우
    if coord[0] < 0 or (R - 1) < coord[0] or coord[1] < 0 or (C - 1) < coord[1]:
        return False
    # 벽에 닿은 경우
    elif field[coord[0]][coord[1]] == "#":
        return False
    return True


def get_reachable_coords(coord: Tuple[int, int]):
    up = (coord[0], coord[1] - 1)
    right = (coord[0] + 1, coord[1])
    down = (coord[0] - 1, coord[1])
    bottom = (coord[0], coord[1] + 1)

    return list(filter(is_reachable, [up, right, down, bottom]))


def bfs(coord):
    queue = deque([coord])

    # 현재 그룹에 속하는 좌표 모음
    group = []

    while queue:
        current = queue.popleft()

        # 중복 탐색 방지
        if visited[current[0]][current[1]] != None:
            continue

        visited[current[0]][current[1]] = coord
        group.append(current)

        reachables = get_reachable_coords(current)

        for reachable in reachables:
            # 중복 탐색 방지
            if visited[current[0]][current[1]] != None:
                queue.append(reachable)

    return group


def who_is_winner(group):
    sheep = 0
    wolf = 0

    for coord in group:
        # 양
        if field[coord[0]][coord[1]] == "o":
            sheep += 1
        elif field[coord[0]][coord[1]] == "v":
            wolf += 1

    if sheep > wolf:
        return (sheep, 0)
    else:
        return (0, wolf)


answer = (0, 0)

for i in range(R):
    for j in range(C):
        # 벽이면 스킵
        if field[i][j] == "#":
            continue
        # 이미 bfs로 방문한 곳이어도 스킵
        if visited[i][j] != None:
            continue

        group = bfs((i, j))

        winner = who_is_winner(group)

        answer = tuple(map(sum, zip(answer, winner)))

print(*answer)

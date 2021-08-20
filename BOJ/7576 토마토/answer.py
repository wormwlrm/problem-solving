import sys
from collections import deque

input = sys.stdin.readline

# 가로 세로
M, N = map(int, input().split())

boxes = []
matured = []

for i in range(N):
    line = list(map(int, input().split()))
    boxes.append(line)

    for j in range(M):
        # 익은 토마토만 기록해둠
        if boxes[i][j] == 1:
            matured.append((i, j))


def valid_child(oy, ox, chy, chx, graph):
    # 맵 오바하는 경우
    if chy < 0 or chx < 0 or N - 1 < chy or M - 1 < chx:
        return False
    # 자기 자신이 아직 안 익은 토마토인 경우
    if graph[oy][ox] == 0:
        return False
    # 벽 또는 이미 익은 경우
    if graph[chy][chx] != 0:
        return False
    return True


def get_children(y, x, graph):
    children = []

    # 상(0), 우(1), 하(2), 좌(3)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for direction in directions:
        dy, dx = direction

        if valid_child(y, x, dy + y, dx + x, graph):
            children.append((dy + y, dx + x))

    return children


def bfs(init, graph):
    answer = -1
    queue = deque(init)

    while queue:
        answer += 1

        for _ in range(len(queue)):
            cy, cx = queue.popleft()
            children = get_children(cy, cx, graph)

            for child in children:
                chy, chx = child
                if graph[chy][chx] == 0:
                    queue.append(child)
                    graph[chy][chx] = answer + 1

    return answer


def not_matured_exist(box):
    for line in box:
        if 0 in line:
            return True
    return False


current_boxes = boxes

turn = bfs(matured, current_boxes)

if not_matured_exist(current_boxes):
    print(-1)
else:
    print(turn)

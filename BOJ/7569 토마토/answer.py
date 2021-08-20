import sys
from collections import deque

input = sys.stdin.readline

# 가로 세로 높이
M, N, H = map(int, input().split())

boxes = []
matured = []

for h in range(H):
    box = []

    for y in range(N):
        line = list(map(int, input().split()))
        box.append(line)

        for x in range(M):
            # 익은 토마토 좌표는 기록해둠
            if box[y][x] == 1:
                matured.append((h, y, x))

    boxes.append(box)


def valid_child(oh, oy, ox, chh, chy, chx, graph):
    # 맵 오바하는 경우
    if chy < 0 or chx < 0 or chh < 0 or N - 1 < chy or M - 1 < chx or H - 1 < chh:
        return False

    # 자기 자신이 아직 안 익은 토마토인 경우
    if graph[oh][oy][ox] == 0:
        return False

    # 벽 또는 이미 익은 경우
    if graph[chh][chy][chx] != 0:
        return False

    return True


def get_children(h, y, x, graph):
    children = []

    # 상, 우, 하, 좌, 위, 아래
    directions = [(0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]

    for direction in directions:
        dh, dy, dx = direction

        if valid_child(h, y, x, dh + h, dy + y, dx + x, graph):
            children.append((dh + h, dy + y, dx + x))

    return children


def bfs(init, graph):
    answer = -1
    queue = deque(init)

    while queue:
        answer += 1

        for _ in range(len(queue)):
            ch, cy, cx = queue.popleft()
            children = get_children(ch, cy, cx, graph)

            for child in children:
                chh, chy, chx = child

                if graph[chh][chy][chx] == 0:
                    queue.append(child)
                    graph[chh][chy][chx] = answer + 1

    return answer


def not_matured_exist(boxes):
    for box in boxes:
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

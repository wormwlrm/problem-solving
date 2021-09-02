import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

area = []

for _ in range(N):
    area.append(list(input().strip()))

visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0] = True

d = [[float("inf") for _ in range(M)] for _ in range(N)]
d[0][0] = 0

queue = deque([(0, 0), None])

answer = 1


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_valid_child(dy, dx):
    # 영역 탈출
    if (dx < 0) or (dy < 0) or M <= dx or N <= dy:
        return False
    # 벽
    elif area[dy][dx] == "0":
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


while queue:
    current = queue.popleft()

    if current == None:
        if len(queue) == 0:
            break

        answer += 1
        queue.append(None)
        continue

    y, x = current

    d[y][x] = answer

    children = get_children(y, x)

    for child in children:
        chy, chx = child

        if visited[chy][chx] == False:
            queue.append(child)
            visited[chy][chx] = True

print(d[N - 1][M - 1])

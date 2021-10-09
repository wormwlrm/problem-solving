import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

area = []

for _ in range(N):
    area.append(list(map(int, list(input()))))

visited = [[[float("inf")] * M for _ in range(N)] for _ in range(2)]
visited[1][0][0] = 1


def get_children(y, x, wall):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    children = []

    for direction in directions:
        dy = y + direction[0]
        dx = x + direction[1]

        if 0 <= dy < N and 0 <= dx < M:
            current = area[dy][dx]

            # 벽 안 뿌수고 그냥 가기
            if current == 0:
                children.append((dy, dx, wall))
            # 벽 뿌수기
            elif current == 1 and wall == 1:
                children.append((dy, dx, wall - 1))

    return children


def bfs(y, x):
    queue = deque([(y, x, 1)])

    turn = 1

    while queue:
        turn += 1

        for _ in range(len(queue)):
            y, x, w = current = queue.popleft()

            children = get_children(y, x, w)

            for child in children:
                chy, chx, chw = child

                # 방문 안했으면 일단 방문
                if visited[chw][chy][chx] == float("inf"):
                    visited[chw][chy][chx] = turn
                    queue.append(child)


bfs(0, 0)

result = min(visited[0][N - 1][M - 1], visited[1][N - 1][M - 1])

if result == float("inf"):
    print(-1)
else:
    print(result)

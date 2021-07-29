import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

paint = []

visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(N):
    paint.append(list(map(int, input().split())))


def get_children(coord):
    global visited

    # 세로
    i = coord[0]
    # 가로
    j = coord[1]

    children = []

    # 위쪽
    if (i - 1 >= 0) and paint[i - 1][j] == 1 and visited[i - 1][j] == False:
        children.append((i - 1, j))
    # 아래쪽
    if (i + 1 < N) and paint[i + 1][j] == 1 and visited[i + 1][j] == False:
        children.append((i + 1, j))
    # 오른쪽
    if (j + 1 < M) and paint[i][j + 1] == 1 and visited[i][j + 1] == False:
        children.append((i, j + 1))
    # 왼쪽
    if (j - 1 >= 0) and paint[i][j - 1] == 1 and visited[i][j - 1] == False:
        children.append((i, j - 1))

    return children


def dfs(coord):
    global visited

    queue = deque([])
    queue.append(coord)

    area = 0

    while queue:
        i, j = queue.popleft()

        if visited[i][j]:
            continue

        visited[i][j] = True
        area += 1

        children = get_children((i, j))
        for ci, cj in children:
            if visited[ci][cj] == False:
                queue.append((ci, cj))

    return area


count = 0
maximum = 0
for i in range(N):
    for j in range(M):
        if paint[i][j] == 0:
            continue
        elif visited[i][j] == True:
            continue

        count += 1
        current = dfs((i, j))

        maximum = max(maximum, current)


print(count)
print(maximum)

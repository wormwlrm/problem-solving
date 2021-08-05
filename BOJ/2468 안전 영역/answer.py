import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

area = []

for _ in range(N):
    area.append(list(map(int, input().split())))

# 높이가 양수인 것만 안 잠긴 것임
def get_underwatered_area(height):
    temp = []

    for arr in area:
        temp.append(arr[::])

    for i in range(N):
        for j in range(N):
            temp[i][j] -= height
    return temp


def get_visited_area():
    return [[0 for _ in range(N)] for _ in range(N)]


def get_children(x, y, area, visited):
    children = []

    # 상
    if (y - 1 >= 0) and visited[y - 1][x] == 0 and area[y - 1][x] > 0:
        children.append((x, y - 1))
    # 하
    if (y + 1 < N) and visited[y + 1][x] == 0 and area[y + 1][x] > 0:
        children.append((x, y + 1))
    # 좌
    if (x - 1 >= 0) and visited[y][x - 1] == 0 and area[y][x - 1] > 0:
        children.append((x - 1, y))
    # 우
    if (x + 1 < N) and visited[y][x + 1] == 0 and area[y][x + 1] > 0:
        children.append((x + 1, y))

    return children


def bfs(x, y, area, visited):
    queue = deque([(x, y)])
    island = 0

    while queue:
        current = queue.popleft()
        x, y = current

        if visited[y][x] == 1:
            continue
        # # 1보다 작으면 침수된 지역
        # elif area[y][x] < 0:
        #     continue

        visited[y][x] = 1
        # 한 번이라도 방문 성공했으면 일단 별개의 땅이 있는 거임
        island = 1

        children = get_children(x, y, area, visited)

        for child in children:
            cx, cy = child
            if visited[cy][cx] == 0:
                queue.append(child)

    return island


def get_area_count(height):
    current_area = get_underwatered_area(height)
    visited = get_visited_area()

    island = 0

    for i in range(N):
        for j in range(N):
            # 이미 방문했으면 그냥 패스
            if visited[j][i]:
                continue
            # 이미 침수됐으면 방문 체크하고 패스
            if current_area[j][i] < 1:
                visited[j][i] = 1
                continue

            island += bfs(i, j, current_area, visited)

    return island


# 아무 지역도 물에 안잠기는 경우 고려
maximum = 1

for height in range(1, 101):
    current = get_area_count(height)
    maximum = max(current, maximum)

print(maximum)

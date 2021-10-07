import sys

input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())

# 0은 빈 공간, 1은 벽, 2는 물
area = [[0] * W for _ in range(H)]

heights = list(map(int, input().split()))

for x in range(W):
    height = H - 1

    for y in range(H):
        if height >= H - heights[x]:
            area[height][x] = 1
        else:
            area[height][x] = 2

        height -= 1


def left_empty(y, x):
    cursor = x
    while 0 <= cursor:
        if area[y][cursor] == 1:
            return False
        cursor -= 1
    return True


def right_empty(y, x):
    cursor = x
    while cursor < W:
        if area[y][cursor] == 1:
            return False
        cursor += 1
    return True


for y in range(H):
    for x in range(W):
        current = area[y][x]

        if current == 1:
            continue

        # 왼쪽 물빠졌으면 현재꺼도 무조건 빠짐
        if 0 < x and area[y][x - 1] == 0:
            area[y][x] = 0

        if left_empty(y, x) or right_empty(y, x):
            area[y][x] = 0

answer = 0

for a in area:
    answer += a.count(2)

print(answer)

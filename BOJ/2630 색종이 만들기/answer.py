import sys

input = sys.stdin.readline

N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]

white = 0

blue = 0


def is_all_white(width, top, left):
    for y in range(top, top + width):
        for x in range(left, left + width):
            # 0이 아닌게 하나라도 있으면 없는 거
            if area[y][x] != 0:
                return 0

    return 1


def is_all_blue(width, top, left):
    for y in range(top, top + width):
        for x in range(left, left + width):
            # 1이 아닌게 하나라도 있으면 없는 거
            if area[y][x] != 1:
                return 0

    return 1


def recursion(width, top, left):
    global white, blue

    all_white = is_all_white(width, top, left)
    if all_white > 0:
        white += all_white
        return

    all_blue = is_all_blue(width, top, left)
    if all_blue > 0:
        blue += all_blue
        return

    # 좌상
    recursion(width // 2, top, left)
    # 우상
    recursion(width // 2, top, left + width // 2)
    # 좌하
    recursion(width // 2, top + width // 2, left)
    # 우하
    recursion(width // 2, top + width // 2, left + width // 2)


recursion(N, 0, 0)

print(white)
print(blue)

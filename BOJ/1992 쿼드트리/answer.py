import sys

input = sys.stdin.readline

N = int(input())

area = [list(input().strip()) for _ in range(N)]


def get_color(width, top, left):
    color = area[top][left]

    for y in range(top, top + width):
        for x in range(left, left + width):
            # 하나라도 색깔 다르면 ㄴㄴ
            if area[y][x] != color:
                return None

    return color


def divide_and_conquer(width, top, left):
    if width == 1:
        return area[top][left]

    color = get_color(width, top, left)

    if color != None:
        return color

    return (
        "("
        + divide_and_conquer(width // 2, top, left)
        + divide_and_conquer(width // 2, top, left + width // 2)
        + divide_and_conquer(width // 2, top + width // 2, left)
        + divide_and_conquer(width // 2, top + width // 2, left + width // 2)
        + ")"
    )


print(divide_and_conquer(N, 0, 0))

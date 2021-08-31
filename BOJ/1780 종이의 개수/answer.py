import sys

input = sys.stdin.readline

N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]

colors = {
    -1: 0,
    0: 0,
    1: 0,
}


def get_color(width, top, left):
    color = area[top][left]

    for y in range(top, top + width):
        for x in range(left, left + width):
            # 하나라도 색깔 다르면 ㄴㄴ
            if area[y][x] != color:
                return None

    return color


def divide_and_conquer(width, top, left):
    color = get_color(width, top, left)

    if color == None:
        # 9등분
        for y in range(3):
            for x in range(3):
                divide_and_conquer(
                    width // 3, top + width // 3 * y, left + width // 3 * x
                )
        return

    colors[color] += 1


divide_and_conquer(N, 0, 0)

print(colors[-1])
print(colors[0])
print(colors[1])

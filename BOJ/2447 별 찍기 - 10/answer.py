import sys

input = sys.stdin.readline

N = int(input())

area = [[" " for _ in range(N)] for _ in range(N)]


def draw(width, top, left):
    if width == 3:
        for y in range(3):
            for x in range(3):
                if (x == 1) and y == 1:
                    continue
                area[top + y][left + x] = "*"
        return

    new_width = width // 3

    draw(new_width, top + new_width * 0, left + new_width * 0)
    draw(new_width, top + new_width * 0, left + new_width * 1)
    draw(new_width, top + new_width * 0, left + new_width * 2)
    draw(new_width, top + new_width * 1, left + new_width * 0)
    # draw(new_width, top + new_width * 1, left + new_width * 1)
    draw(new_width, top + new_width * 1, left + new_width * 2)
    draw(new_width, top + new_width * 2, left + new_width * 0)
    draw(new_width, top + new_width * 2, left + new_width * 1)
    draw(new_width, top + new_width * 2, left + new_width * 2)


draw(N, 0, 0)

for line in area:
    print("".join(line))

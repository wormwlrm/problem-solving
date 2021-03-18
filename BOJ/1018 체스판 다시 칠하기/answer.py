x, y = map(int, input().split())

coords = list([])

for i in range(x):
    row = str(input())
    arr = []

    for j in list(row):
        arr.append(j)

    coords.append(arr)

min_diff = 50 * 50


def coord_start_with(char1, char2):
    return [[char1, char2] * 4, [char2, char1] * 4] * 4


def calc(x1, y1):
    global min_diff
    global coords

    start_with_black = coord_start_with("B", "W")
    start_with_white = coord_start_with("W", "B")

    current_coord = [[None] * 8 for _ in range(8)]

    for coord2 in [start_with_black, start_with_white]:
        current_diff = 0

        for i in range(0, 8):
            for j in range(0, 8):
                current_coord[i][j] = coords[x1 + i][y1 + j]

                if (current_coord[i][j] != coord2[i][j]):
                    current_diff += 1

        if (current_diff < min_diff):
            min_diff = current_diff


for i in range(0, x - 7):
    for j in range(0, y - 7):
        calc(i, j)

print(min_diff)

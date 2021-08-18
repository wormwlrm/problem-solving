import sys

input = sys.stdin.readline

N, M = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(N)]

types = {
    "O": [[[1, 1], [1, 1]]],
    "I": [
        [
            [1, 1, 1, 1],
        ],
        [[1], [1], [1], [1]],
    ],
    "Z": [
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1, 1], [1, 1, 0]],
        [[0, 1], [1, 1], [1, 0]],
        [[1, 0], [1, 1], [0, 1]],
    ],
    "L": [
        [[1, 0, 0], [1, 1, 1]],
        [[0, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 0]],
        [[1, 1, 1], [0, 0, 1]],
        [[1, 1], [1, 0], [1, 0]],
        [[1, 1], [0, 1], [0, 1]],
        [[0, 1], [0, 1], [1, 1]],
        [[1, 0], [1, 0], [1, 1]],
    ],
    "T": [
        [[1, 1, 1], [0, 1, 0]],
        [[0, 1, 0], [1, 1, 1]],
        [[1, 0], [1, 1], [1, 0]],
        [[0, 1], [1, 1], [0, 1]],
    ],
}


class Block:
    def __init__(self, type) -> None:
        self.cursors = types[type]

    def calc_area(self, y, x):
        maximum = -1

        for cursor in self.cursors:
            ry = len(cursor)
            rx = len(cursor[0])

            current = 0

            try:
                for cy in range(ry):
                    for cx in range(rx):
                        # # 인덱스 초과하면 못 만드는 경우임
                        # if y + cy > N - 1 or x + cx > M - 1:
                        #     raise
                        if cursor[cy][cx] == 1:
                            current += area[y + cy][x + cx]
            except:
                current = -1
            finally:
                maximum = max(maximum, current)

        return maximum


max_area = 0

# 블록 종류
for type in types.keys():
    block = Block(type)
    current = 0

    for cursor in block.cursors:
        # 커서 세로 길이
        ry = len(cursor)
        # 커서 가로 길이
        rx = len(cursor[0])

        # 영역 세로
        for j in range(0, N - ry + 1):
            # 영역 가로
            for i in range(0, M - rx + 1):
                max_area = max(max_area, block.calc_area(j, i))

print(max_area)

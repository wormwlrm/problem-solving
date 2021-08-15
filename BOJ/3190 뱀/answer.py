import sys
from collections import deque

input = sys.stdin.readline


N = int(input())


class Area:
    def __init__(self, apples) -> None:
        self.coord = [[" "] * N for _ in range(N)]

        for row, col in apples:
            self.coord[row][col] = "A"

    def is_apple(self, coord) -> bool:
        row, col = coord
        return self.coord[row][col] == "A"

    def clear(self):
        for row in range(N):
            for col in range(N):
                if self.coord[row][col] in [" ", "H", "T"]:
                    self.coord[row][col] = ""


K = int(input())

apples = []

for _ in range(K):
    row, column = map(int, input().split())
    apples.append((row - 1, column - 1))

area = Area(apples)


L = int(input())

turning = [None] * 10001

for _ in range(L):
    X, C = map(str, input().split())
    turning[int(X)] = C


class Snake:
    # 상(0), 우(1), 하(2), 좌(3)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, turning) -> None:
        self.direction = 1
        self.coords = deque([(0, 0)])
        self.turn = 0
        self.turning = turning
        area.coord[0][0] = "H"

    def get_head(self):
        return self.coords[0]

    def get_next_block(self):
        row, col = self.get_head()
        dr, dc = self.directions[self.direction]
        return (
            row + dr,
            col + dc,
        )

    def movable(self, coord):
        row, col = coord
        # 몸 만나는 경우
        for body_row, body_col in self.coords:
            if body_row == row and body_col == col:
                return False
        # 벽 만나는 경우
        if row < 0 or N <= row or col < 0 or N <= col:
            return False

        return True

    def need_change_direction(self) -> bool:
        return self.turning[self.turn] != None

    def change_direction(self):
        # 좌회전
        if self.turning[self.turn] == "L":
            self.direction = (self.direction - 1) % 4

        # 우회전
        elif self.turning[self.turn] == "D":
            self.direction = (self.direction + 1) % 4

    def sync_with_map(self):
        area.clear()

        for index, value in enumerate(self.coords):
            # 머리는 H
            row, col = value
            if index == 0:
                area.coord[row][col] = "H"
            else:
                area.coord[row][col] = "T"

    def move(self):
        next_block = self.get_next_block()

        # 벽 만나거나 꼬리 만나는 경우 게임 오바
        if not self.movable(next_block):
            return self.turn + 1

        # 사과 만날 때
        if area.is_apple(next_block):
            # 현재 칸을 제일 왼쪽에 머리로 붙임
            self.coords.appendleft(next_block)
        # 그냥
        else:
            # 꼬리는 한 칸 뗌
            self.coords.pop()
            # 현재 칸을 제일 왼쪽에 머리로 붙임
            self.coords.appendleft(next_block)

        # 지도와 싱크 맞춰 줌
        self.turn += 1
        self.sync_with_map()

        if self.need_change_direction():
            self.change_direction()

        return None


snake = Snake(turning)

while True:
    game_over = snake.move()

    if game_over != None:
        print(game_over)
        break

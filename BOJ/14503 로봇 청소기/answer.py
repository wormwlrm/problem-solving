import sys
from enum import Enum
from copy import deepcopy

input = sys.stdin.readline

row, col = map(int, input().split())

cleaner_row, cleaner_col, direction = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(row)]


class Status(Enum):
    dirty = 0
    wall = 1
    cleaned = 2


class Area:
    def __init__(self, arr) -> None:
        self.floor = deepcopy(arr)

    def get_cleaned(self):
        acc = 0
        for i in range(row):
            for j in range(col):
                if self.floor[i][j] == Status.cleaned.value:
                    acc += 1
        return acc


area = Area(arr)


class Cleaner:
    # 상(0), 우(1), 하(2), 좌(3)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, row, col, direction) -> None:
        self.row = row
        self.col = col
        self.direction = direction

    def clean(self):
        # 자기 현재 위치 청소하기
        area.floor[self.row][self.col] = Status.cleaned.value

    def get_around_block(self):
        # 앞, 좌, 뒤, 우 순서로 나옴
        blocks = []

        for i in range(4):
            temp_direction = (self.direction - i) % 4

            temp_row = self.row + self.directions[temp_direction][0]
            temp_col = self.col + self.directions[temp_direction][1]

            blocks.append(area.floor[temp_row][temp_col])

        return blocks

    def turn_left(self):
        # 왼쪽으로 방향 돌리기
        self.direction = (self.direction - 1) % 4

    def go_straight(self):
        # 현재 보고 있는 방향으로 이동
        self.row = self.row + self.directions[self.direction][0]
        self.col = self.col + self.directions[self.direction][1]

    def go_backward(self):
        # 뒤로 두 칸 후진
        backward = (self.direction - 2) % 4
        self.row = self.row + self.directions[backward][0]
        self.col = self.col + self.directions[backward][1]

    def move(self):
        # 자기 자리 청소
        self.clean()

        forward, left, backward, right = self.get_around_block()

        # 왼쪽 자리가 청소하지 않은 칸 있으면 회전 후 이동
        if left in [Status.dirty.value]:
            self.turn_left()
            self.go_straight()
            return True

        # 상하좌우 중 청소 가능한 자리가 있긴 하면 왼쪽으로 회전만
        if left in [Status.wall.value, Status.cleaned.value] and (
            backward in [Status.dirty.value]
            or right in [Status.dirty.value]
            or forward in [Status.dirty.value]
        ):
            self.turn_left()
            return True

        # 후진 가능한 경우
        if backward in [Status.dirty.value, Status.cleaned.value]:
            self.go_backward()
            return True

        # 후진도 못 하는 경우 끝
        if backward in [Status.wall.value]:
            return False


cleaner = Cleaner(cleaner_row, cleaner_col, direction)


while True:
    result = cleaner.move()

    if result == False:
        break

print(area.get_cleaned())

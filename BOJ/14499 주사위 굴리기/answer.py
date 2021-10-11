# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/14499%20%EC%A3%BC%EC%82%AC%EC%9C%84%20%EA%B5%B4%EB%A6%AC%EA%B8%B0

import sys

input = lambda: sys.stdin.readline().rstrip()

# 세로, 가로, y좌표, x좌표, 명령 갯수
N, M, y, x, K = map(int, input().split())

area = []

for _ in range(N):
    area.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

direction = {"E": 1, "W": 2, "N": 3, "S": 4}


class Dice:
    def __init__(self, y, x) -> None:
        self.top = 0
        self.bottom = 0
        self.east = 0
        self.west = 0
        self.north = 0
        self.south = 0

        self.y = y
        self.x = x

    def get_temp_coord(self, d):
        if d == direction["E"]:
            return (self.y, self.x + 1)
        elif d == direction["W"]:
            return (self.y, self.x - 1)
        elif d == direction["N"]:
            return (self.y - 1, self.x)
        elif d == direction["S"]:
            return (self.y + 1, self.x)
        else:
            return 0

    def can_roll(self, d):
        ty, tx = self.get_temp_coord(d)
        return 0 <= ty < N and 0 <= tx < M

    def roll(self, d):
        # 동
        if d == direction["E"]:
            self.top, self.east, self.bottom, self.west = (
                self.west,
                self.top,
                self.east,
                self.bottom,
            )
        # 서
        elif d == direction["W"]:
            self.top, self.east, self.bottom, self.west = (
                self.east,
                self.bottom,
                self.west,
                self.top,
            )
        # 북
        elif d == direction["N"]:
            self.top, self.north, self.bottom, self.south = (
                self.south,
                self.top,
                self.north,
                self.bottom,
            )
        # 남
        elif d == direction["S"]:
            self.top, self.north, self.bottom, self.south = (
                self.north,
                self.bottom,
                self.south,
                self.top,
            )
        else:
            return 0

    def check(self):
        # 바닥이 0이면 주사위가 바닥에 복사됨
        if area[self.y][self.x] == 0:
            area[self.y][self.x] = self.bottom
        # 바닥에 숫자 있으면 바닥이 주사위가 옮겨지고 바닥은 0이 됨
        else:
            self.bottom = area[self.y][self.x]
            area[self.y][self.x] = 0

    def print(self):
        # top만 출력함
        print(self.top)

    def execute(self, d) -> int:
        if not self.can_roll(d):
            return

        self.y, self.x = self.get_temp_coord(d)

        self.roll(d)
        self.check()
        self.print()


dice = Dice(y, x)

for command in commands:
    dice.execute(command)

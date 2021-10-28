# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2573%20%EB%B9%99%EC%82%B0

import sys
from collections import deque


input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

area = []

glaciers = []

for row in range(N):
    line = list(map(int, input().split()))

    for col in range(M):
        if line[col] > 0:
            glaciers.append((row, col))

    area.append(line)


class Glacier:
    def __init__(self, area, glaciers) -> None:
        self.area = area
        self.glaciers = glaciers
        self.turn = 0

    def get_melt_amount(self):
        temp = [[0 for _ in range(M)] for _ in range(N)]

        for y, x in self.glaciers:
            melt_amount = 0
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                ny, nx = dy + y, dx + x
                if area[ny][nx] == 0:
                    melt_amount += 1

            temp[y][x] = melt_amount

        return temp

    def update_glaciers(self, melt_amount):
        glaciers = []

        for y, x in self.glaciers:
            if self.area[y][x] - melt_amount[y][x] > 0:
                glaciers.append((y, x))
                self.area[y][x] -= melt_amount[y][x]
            else:
                self.area[y][x] = 0

        self.glaciers = glaciers

    def is_connected(self):
        if len(self.glaciers) == 0:
            return True

        queue = deque([self.glaciers[0]])
        visited = {self.glaciers[0]: True}

        while queue:
            y, x = queue.popleft()

            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = dy + y, dx + x

                if (
                    0 <= ny < N
                    and 0 <= nx < M
                    and self.area[ny][nx] > 0
                    and (ny, nx) not in visited
                ):
                    queue.append((ny, nx))
                    visited[(ny, nx)] = True

        return len(self.glaciers) == len(visited)

    def run(self) -> None:
        melt_amount = self.get_melt_amount()
        self.update_glaciers(melt_amount)
        self.turn += 1


simulator = Glacier(area, glaciers)

while len(simulator.glaciers) > 0:
    if not simulator.is_connected():
        print(simulator.turn)
        exit()

    simulator.run()


print(0)

# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/17144%20%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80%20%EC%95%88%EB%85%95

import sys

input = lambda: sys.stdin.readline().rstrip()

R, C, T = map(int, input().split())


class Simulator:
    def __init__(self, area, cleaners):
        self.area = area
        self.cleaners = cleaners
        self.turn = 0
        self.flow_top = self.get_cleaner_route("top")
        self.flow_bottom = self.get_cleaner_route("bottom")

    def get_cleaner_route(self, direction):
        if direction == "top":
            # 위쪽 공기 흐름
            # 오른쪽, 위쪽, 왼쪽, 아래쪽 순서
            directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
            routes = [self.cleaners[0]]
        else:
            # 아래쪽 공기 흐름
            # 오른쪽, 아래쪽, 왼쪽, 위쪽 순서
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            routes = [self.cleaners[1]]

        for dy, dx in directions:
            cy, cx = routes[-1]

            while True:
                ny, nx = cy + dy, cx + dx

                if 0 <= ny < R and 0 <= nx < C and (ny, nx) not in routes:
                    routes.append((ny, nx))
                    cy, cx = ny, nx
                else:
                    break

        return routes

    def get_spread_dust_area(self):
        diff = [[0] * C for _ in range(R)]

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for y in range(R):
            for x in range(C):
                # 먼지 없거나 공기청정기인 경우에는 패스
                if self.area[y][x] in [0, -1]:
                    continue

                spread_amount = self.area[y][x] // 5

                if spread_amount == 0:
                    continue

                for dy, dx in directions:
                    ny, nx = y + dy, x + dx

                    # 확산 가능하다면
                    if 0 <= ny < R and 0 <= nx < C and area[ny][nx] != -1:
                        # 확산되는 거에는 더하고
                        diff[ny][nx] += spread_amount
                        # 원래 값은 뺀다
                        diff[y][x] -= spread_amount

        return diff

    def run_cleaner(self, area):
        for flows in [self.flow_top[::-1], self.flow_bottom[::-1]]:
            flowed_values = []

            for index in range(len(flows) - 1):
                if index == len(flows) - 1:
                    flowed_values.append(0)
                else:
                    ny, nx = flows[index + 1]
                    flowed_values.append(area[ny][nx])

            for index, value in enumerate(flows):
                if index == len(flows) - 1:
                    continue
                # 새로 나온 공기는 청소됨
                if index == len(flows) - 2:
                    area[value[0]][value[1]] = 0
                    continue

                area[value[0]][value[1]] = flowed_values[index]

    def add_diff(self, diff):
        for r in range(R):
            for c in range(C):
                self.area[r][c] += diff[r][c]

    def run(self):
        diff = self.get_spread_dust_area()
        self.add_diff(diff)
        self.run_cleaner(self.area)
        self.turn += 1

    def get_dust_amount(self):
        # 청소기 -1 이 2개이므로 2 더해줌
        return sum(sum(row) for row in self.area) + 2


area = []

cleaner = []

for row in range(R):
    line = list(map(int, input().split()))

    for index, item in enumerate(line):
        if item == -1:
            cleaner.append((row, index))

    area.append(line)

simulator = Simulator(area, cleaner)

for _ in range(T):
    simulator.run()

print(simulator.get_dust_amount())

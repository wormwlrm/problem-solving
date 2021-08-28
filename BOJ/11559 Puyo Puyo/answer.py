import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

maps = []

for _ in range(12):
    maps.append(list(input().strip()))


class Area:
    # 상(0), 우(1), 하(2), 좌(3)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    colors = ["R", "G", "B", "P", "Y"]

    def __init__(self, area):
        self.area = deepcopy(area)
        self.chain = 0

    def is_valid_child(self, origin_color, y, x):
        if (y < 0) or (x < 0) or 12 <= y or 6 <= x:
            return False

        if self.area[y][x] != origin_color:
            return False

        return True

    def get_children(self, origin_color, y, x):
        children = []

        for direction in self.directions:
            dy = direction[0] + y
            dx = direction[1] + x

            if self.is_valid_child(origin_color, dy, dx):
                children.append((dy, dx))

        return children

    def bfs(self, y, x, visited):

        visited[y][x] = True

        queue = deque([(y, x)])
        origin_color = self.area[y][x]

        group = []

        while queue:
            current = queue.popleft()
            group.append(current)

            cy, cx = current
            children = self.get_children(origin_color, cy, cx)

            for child in children:
                chy, chx = child

                if visited[chy][chx] == False:
                    visited[chy][chx] = True
                    queue.append(child)

        return group

    def search(self) -> bool:
        visited = [[False] * 6 for _ in range(12)]
        group = []

        for y in range(12):
            for x in range(6):
                if self.area[y][x] == ".":
                    continue

                current = self.bfs(y, x, visited)

                if len(current) >= 4:
                    group.append(current)

        return group

    def crash(self, groups):
        for group in groups:
            for y, x in group:
                self.area[y][x] = "."

        return self

    def push_down(self):
        for x in range(6):
            bottom = 11

            for y in range(11, -1, -1):
                if bottom == y and self.area[y][x] in self.colors:
                    bottom -= 1
                    continue

                if self.area[y][x] == ".":
                    continue

                self.area[bottom][x] = self.area[y][x]
                self.area[y][x] = "."
                bottom -= 1

    def do(self):
        groups = self.search()

        if len(groups) == 0:
            return False

        self.crash(groups)
        self.push_down()
        self.chain += 1

        return True


area = Area(maps)

status = True

while status:
    status = area.do()

print(area.chain)

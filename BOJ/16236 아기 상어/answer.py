import sys
from math import isinf
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]


def get_shark_coord():
    for y in range(N):
        for x in range(N):
            if area[y][x] == 9:
                return (y, x)


shark_y, shark_x = get_shark_coord()


class Shark:
    # 상(0), 우(1), 하(2), 좌(3)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, y, x) -> None:
        self.size = 2
        self.stomache = 0
        self.distance = [[float("inf")] * N for _ in range(N)]
        self.y = y
        self.x = x
        self.edibles = []
        self.turn = 0

    def is_valid_child(self, graph, oy, ox, dy, dx):
        # 영역 탈출
        if (dx < 0) or (dy < 0) or N <= dx or N <= dy:
            return False
        # 큰 물고기
        elif area[dy][dx] > self.size:
            return False
        return True

    def is_edible(self, y, x):
        return area[y][x] in [1, 2, 3, 4, 5, 6] and area[y][x] < self.size

    def get_children(self, graph, oy, ox):
        children = []

        for direction in self.directions:
            dy = direction[0] + oy
            dx = direction[1] + ox

            if self.is_valid_child(graph, oy, ox, dy, dx):
                children.append((dy, dx))

        return children

    def reset_distance(self):
        distance = [[float("inf")] * N for _ in range(N)]
        distance[self.y][self.x] = 0

        queue = deque([(self.y, self.x), None])
        depth = 1

        edibles = []

        while queue:
            current = queue.popleft()

            if current == None:
                depth += 1

                if len(queue) > 0:
                    queue.append(None)

                continue

            y, x = current

            if self.is_edible(y, x):
                edibles.append((y, x, depth - 1))

            children = self.get_children(distance, y, x)

            for child in children:
                cy, cx = child
                if isinf(distance[cy][cx]):
                    queue.append(child)
                    distance[cy][cx] = depth

        self.distance = deepcopy(distance)

        # 가까운 물고기, 위에 있는 물고기, 왼쪽에 있는 물고기
        self.edibles = sorted(edibles, key=lambda x: (x[2], x[0], x[1]))

    def hunt(self):
        self.reset_distance()

        if len(self.edibles) == 0:
            return False

        ty, tx, td = self.edibles[0]

        # 자리 옮기기
        area[self.y][self.x] = 0
        area[ty][tx] = 9

        # 물고기 먹기
        self.stomache += 1

        if self.is_full():
            self.size_up()

        self.x = tx
        self.y = ty
        self.turn += td

        return True

    def is_full(self):
        return self.size == self.stomache

    def size_up(self):
        self.size += 1
        self.stomache = 0


shark = Shark(shark_y, shark_x)

state = True

while state:
    state = shark.hunt()

print(shark.turn)

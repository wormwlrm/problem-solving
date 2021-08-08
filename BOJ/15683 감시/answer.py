import sys
import copy

input = sys.stdin.readline

H, W = map(int, input().split())

area = []

cctvs = []

walls = 0


class CCTV:
    def __init__(self, h, w, kind) -> None:
        self.h = h
        self.w = w
        self.kind = kind
        self.search_ways = []

        self.calculate_kind()

    def calculate_kind(self):
        if self.kind == 1:
            self.search_ways.append(["up"])
            self.search_ways.append(["down"])
            self.search_ways.append(["left"])
            self.search_ways.append(["right"])
        elif self.kind == 2:
            self.search_ways.append(["up", "down"])
            self.search_ways.append(["right", "left"])
        elif self.kind == 3:
            self.search_ways.append(["up", "right"])
            self.search_ways.append(["right", "down"])
            self.search_ways.append(["down", "left"])
            self.search_ways.append(["left", "up"])
        elif self.kind == 4:
            self.search_ways.append(["up", "right", "down"])
            self.search_ways.append(["right", "down", "left"])
            self.search_ways.append(["down", "left", "up"])
            self.search_ways.append(["left", "up", "right"])
        elif self.kind == 5:
            self.search_ways.append(["up", "right", "down", "left"])


for h in range(H):
    line = list(map(int, input().split()))
    area.append(line)

for h in range(H):
    for w in range(W):
        item = area[h][w]
        if 1 <= item <= 5:
            cctv = CCTV(h, w, item)
            cctvs.append(cctv)
        elif item == 6:
            walls += 1

minimum = float("inf")


def apply(h, w, search_ways, origin):
    # 방문함
    temp = copy.deepcopy(origin)

    for direction in search_ways:

        if direction == "up":
            for i in range(h, -1, -1):
                # 벽 만나면 탈출
                if area[i][w] == 6:
                    break
                temp[i][w] = 1
        if direction == "down":
            for i in range(h, H):
                # 벽 만나면 탈출
                if area[i][w] == 6:
                    break
                temp[i][w] = 1
        if direction == "right":
            for i in range(w, W):
                # 벽 만나면 탈출
                if area[h][i] == 6:
                    break
                temp[h][i] = 1
        if direction == "left":
            for i in range(w, -1, -1):
                # 벽 만나면 탈출
                if area[h][i] == 6:
                    break
                temp[h][i] = 1
    return temp


def search(index, prev_map):
    global minimum

    current_map = copy.deepcopy(prev_map)

    if index > len(cctvs) - 1:
        # 계산
        value = calc_undetectable_area(current_map)
        minimum = min(minimum, value - walls)
    else:
        cctv_h = cctvs[index].h
        cctv_w = cctvs[index].w
        search_ways = cctvs[index].search_ways

        for way in search_ways:
            temp = apply(cctv_h, cctv_w, way, current_map)
            search(index + 1, temp)


def calc_undetectable_area(maps):
    acc = 0
    for h in range(H):
        for w in range(W):
            if maps[h][w] == 0:
                acc += 1
    return acc


visited = [[0 for _ in range(W)] for _ in range(H)]

search(0, visited)

print(minimum)

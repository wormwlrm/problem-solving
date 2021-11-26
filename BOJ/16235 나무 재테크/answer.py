# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/16235%20%EB%82%98%EB%AC%B4%20%EC%9E%AC%ED%85%8C%ED%81%AC

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

# N은 맵 크기, M은 나무 수, K는 년도
N, M, K = map(int, input().split())

fertilizer = []

for _ in range(N):
    fertilizer.append(list(map(int, input().split())))

trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    y, x, age = map(int, input().split())
    trees[y - 1][x - 1].append(age)


class Simulator:
    def __init__(self, fertilizer, trees) -> None:
        self.soil = [[5 for _ in range(N)] for _ in range(N)]
        self.fertilizer = fertilizer
        self.trees = trees
        self.turn = 0

        pass

    def run(self):
        self.turn += 1
        self.spring_summer()
        self.autumn_winter()

    def spring_summer(self):
        for y in range(N):
            for x in range(N):
                len_t = len(self.trees[y][x])
                for k in range(len_t):
                    if self.trees[y][x][k] <= self.soil[y][x]:
                        self.soil[y][x] -= trees[y][x][k]
                        self.trees[y][x][k] += 1
                    else:
                        for _ in range(k, len_t):
                            self.soil[y][x] += self.trees[y][x].pop() // 2
                        break

    def autumn_winter(self):
        # 8방향
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

        for y in range(N):
            for x in range(N):
                for k in self.trees[y][x]:
                    if k % 5 == 0:
                        for direction in directions:
                            ny, nx = y + direction[0], x + direction[1]
                            if 0 <= ny < N and 0 <= nx < N:
                                self.trees[ny][nx].appendleft(1)
                self.soil[y][x] += self.fertilizer[y][x]


simulator = Simulator(fertilizer, trees)

for _ in range(K):
    simulator.run()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(simulator.trees[i][j])

print(answer)

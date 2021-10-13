# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2580%20%EC%8A%A4%EB%8F%84%EC%BF%A0

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

sudoku = []

points = deque([])

for y in range(9):
    line = list(map(int, input().split()))

    for index, value in enumerate(line):
        if value == 0:
            points.append((y, index))

    sudoku.append(line)


def horizontal_check(y, x):
    global sudoku

    horizontal = sudoku[y]
    available = list(range(1, 10))

    for i in horizontal:
        if i in available:
            available.remove(i)

    return available


def vertical_check(y, x):
    global sudoku

    vertical = []
    for line in sudoku:
        vertical.append(line[x])

    available = list(range(1, 10))

    for i in vertical:
        if i in available:
            available.remove(i)

    return available


def group_check(y, x):
    global sudoku

    group = []

    left, top = (y // 3) * 3, (x // 3) * 3

    for i in range(3):
        for j in range(3):
            group.append(sudoku[left + i][top + j])

    available = list(range(1, 10))

    for i in group:
        if i in available:
            available.remove(i)

    return available


def determinable(y, x):
    global sudoku

    horizontal = horizontal_check(y, x)
    vertical = vertical_check(y, x)
    group = group_check(y, x)

    return sorted(list(set(horizontal) & set(vertical) & set(group)))


def print_sudoku():
    for line in sudoku:
        print(" ".join(map(str, line)))


def dfs():
    global sudoku, points

    if len(points) == 0:
        print_sudoku()
        exit()

    y, x = point = points.popleft()

    methods = determinable(y, x)

    for method in methods:
        sudoku[y][x] = method
        dfs()
        sudoku[y][x] = 0

    points.appendleft(point)


dfs()

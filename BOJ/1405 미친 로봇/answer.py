# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1405%20%EB%AF%B8%EC%B9%9C%20%EB%A1%9C%EB%B4%87

import sys

input = lambda: sys.stdin.readline().rstrip()

count, E, W, S, N = map(int, input().split())

prob = {0: E, 1: W, 2: S, 3: N}

visited = {(0, 0): True}


def recursive(current, probability, depth):
    global prob

    y, x = current

    if depth == count:
        return probability

    acc = 0

    for index, direction in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
        ny, nx = y + direction[0], x + direction[1]

        if (ny, nx) in visited:
            continue

        visited[(ny, nx)] = True
        acc += recursive((ny, nx), probability * prob[index] / 100, depth + 1)
        del visited[(ny, nx)]

    return acc


print(recursive((0, 0), 1, 0))

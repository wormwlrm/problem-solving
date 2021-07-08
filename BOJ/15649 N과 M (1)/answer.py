import sys
from collections import deque

input = sys.stdin.readline

visited = deque([])

N, M = map(int, input().rstrip().split())


# 방문한 적 없음
def promising(index):
    return not is_visited(index)


# 방문했는지
def is_visited(index):
    return index in visited


def locate(index):
    global visited

    visited.append(index)

    if len(visited) == M:
        print(*visited)
        return

    for j in range(1, N + 1):
        if promising(j):
            locate(j)
            visited.pop()


for i in range(1, N + 1):
    locate(i)
    visited.pop()

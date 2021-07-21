import sys
from collections import deque
from typing import Tuple

input = sys.stdin.readline

cases = int(input())


def not_completed(visited, end):
    return end not in visited


for case in range(cases):
    width = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    queue = deque([start, None])

    depth = 0

    visited = {}

    def is_reachable(origin: Tuple[int, int]):
        if (
            origin[0] < 0
            or (width - 1) < origin[0]
            or origin[1] < 0
            or (width - 1) < origin[1]
        ):
            return False
        return True

    def get_reachable_coords(origin: Tuple[int, int]):
        coord1 = (origin[0] + 1, origin[1] + 2)
        coord2 = (origin[0] + 2, origin[1] + 1)
        coord3 = (origin[0] + 2, origin[1] - 1)
        coord4 = (origin[0] + 1, origin[1] - 2)
        coord5 = (origin[0] - 1, origin[1] + 2)
        coord6 = (origin[0] - 2, origin[1] + 1)
        coord7 = (origin[0] - 2, origin[1] - 1)
        coord8 = (origin[0] - 1, origin[1] - 2)

        return list(
            filter(
                is_reachable,
                [coord1, coord2, coord3, coord4, coord5, coord6, coord7, coord8],
            )
        )

    while not_completed(visited, end):
        current = queue.popleft()

        # 깊이 기록용
        if current == None:
            depth += 1
            queue.append(None)
            continue
        # 중복 탐색 방지
        elif current in visited:
            continue

        visited[current] = depth

        reachables = get_reachable_coords(current)

        for reachable in reachables:
            # 중복 탐색 방지
            if reachable not in visited:
                queue.append(reachable)

    print(visited[end])

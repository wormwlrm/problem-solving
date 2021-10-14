# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1520%20%EB%82%B4%EB%A6%AC%EB%A7%89%20%EA%B8%B8

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(M)]

queue = [(-area[0][0], 0, 0)]


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

dp = [[0] * N for _ in range(M)]
dp[0][0] = 1

on_queue = [[False] * N for _ in range(M)]


def bfs():

    turn = -1

    while queue:
        turn += 1

        for _ in range(len(queue)):
            height, y, x = current = heapq.heappop(queue)

            if (y, x) != (0, 0) and dp[y][x] > 0:
                continue

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                if 0 <= ny < M and 0 <= nx < N:
                    weight = area[ny][nx]

                    # 가리키는 방향이 현재보다 큰 거라면 갯수 더하기
                    if weight > area[y][x]:
                        dp[y][x] += dp[ny][nx]

                    # 아니라면 큐에 넣기
                    elif dp[ny][nx] == 0 and on_queue[ny][nx] == False:
                        on_queue[ny][nx] = True
                        heapq.heappush(queue, (-weight, ny, nx))


bfs()

print(dp[-1][-1])

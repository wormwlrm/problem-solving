# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1092%20%EB%B0%B0

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())


cranes = sorted(list(map(int, input().split())), reverse=True)

M = int(input())

trailers = sorted(list(map(int, input().split())), reverse=True)

# 트레일러로 옮길 수 없는 게 하나라도 있다면
if trailers[0] > cranes[0]:
    print(-1)
    exit(0)

turn = 0

visited = [False] * M

while sum(visited) != M:
    turn += 1
    crane_index = 0
    trailer_index = 0

    # 크레인 다 싣거나, 트레일러 탐색할때까지
    while crane_index < N and trailer_index < M:
        # 이미 싣은 거면 패스
        if visited[trailer_index]:
            trailer_index += 1
            continue

        # 싣을 수 있으면 담기
        if cranes[crane_index] >= trailers[trailer_index]:
            visited[trailer_index] = True
            crane_index += 1
            trailer_index += 1
        else:
            trailer_index += 1

print(turn)

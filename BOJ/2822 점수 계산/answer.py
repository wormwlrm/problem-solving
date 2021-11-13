# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2822%20%EC%A0%90%EC%88%98%20%EA%B3%84%EC%82%B0

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

queue = []

for i in range(1, 9):
    heapq.heappush(queue, (-int(input()), i))

points = 0
answer = []

for _ in range(5):
    point, idx = heapq.heappop(queue)
    points += point
    answer.append(idx)

print(-points)
print(*sorted(answer))
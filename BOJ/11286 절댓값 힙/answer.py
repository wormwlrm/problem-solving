import sys
import heapq

input = sys.stdin.readline

N = int(input())

queue = []


def heap_print():
    if len(queue) == 0:
        return (0, 0)

    return heapq.heappop(queue)


for _ in range(N):
    command = int(input())

    if command == 0:
        prior, origin = heap_print()
        print(origin)
        continue

    heapq.heappush(queue, (abs(command), command))

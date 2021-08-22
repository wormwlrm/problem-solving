import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = []


def zero():
    if len(arr) == 0:
        print(0)
        return

    print(-heapq.heappop(arr))


for _ in range(N):
    command = int(input())

    if command == 0:
        zero()
    else:
        heapq.heappush(arr, -command)

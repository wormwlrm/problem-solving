import sys
import heapq

input = sys.stdin.readline

N = int(input())

cursor = []

for i in list(map(int, input().split())):
    heapq.heappush(cursor, i)

for i in range(1, N):
    arr = list(map(int, input().split()))

    for j in arr:
        heapq.heappush(cursor, j)
        heapq.heappop(cursor)

print(heapq.heappop(cursor))

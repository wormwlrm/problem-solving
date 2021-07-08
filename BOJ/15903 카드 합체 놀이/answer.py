import sys
from queue import PriorityQueue

input = sys.stdin.readline

q = PriorityQueue()

N, M = map(int, input().rstrip().split())

cards = list(map(int, input().rstrip().split()))

for i in cards:
    q.put(i)

for i in range(M):
    first = q.get()
    second = q.get()

    q.put(first + second)
    q.put(first + second)

result = 0

while not q.empty():
    result += q.get()

print(result)

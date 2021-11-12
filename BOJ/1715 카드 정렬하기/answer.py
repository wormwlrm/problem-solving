# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1715%20%EC%B9%B4%EB%93%9C%20%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0

import sys
from queue import PriorityQueue

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

q = PriorityQueue()

for _ in range(N):
    q.put(int(input()))

count = 0

while q and q.qsize() > 1:
    first, second = q.get(), q.get()

    count += first + second

    q.put(first + second)

print(count)

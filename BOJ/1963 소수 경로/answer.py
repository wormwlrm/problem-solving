# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1963%20%EC%86%8C%EC%88%98%20%EA%B2%BD%EB%A1%9C

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def sieve_of_eratosthenes():
    start = 1000
    n = 10000

    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    from_start = {}
    for i in range(start + 1, n + 1, 2):
        if numbers[i]:
            from_start[i] = True

    return from_start


primes = sieve_of_eratosthenes()


def bfs(start, end):
    queue = deque([start])
    visited = [float("inf")] * 9001
    depth = -1

    while queue:
        depth += 1
        for _ in range(len(queue)):
            current = queue.popleft()

            visited[current - 1000] = min(depth, visited[current - 1000])

            if current == end:
                return depth

            for digit in range(4):
                # 첫째자리 변환은 1부터 9까지
                if digit == 0:
                    numbers = range(1, 10)
                else:
                    numbers = range(10)

                # 나머지는 0부터 9까지
                for i in numbers:
                    temp = str(current)
                    temp = int(temp[:digit] + str(i) + temp[digit + 1 :])

                    if temp == current:
                        continue

                    if (temp in primes) and (visited[temp - 1000] == float("inf")):
                        queue.append(temp)
    return "impossible"


T = int(input())

for _ in range(T):
    S, E = map(int, input().split())

    if S == E:
        print(0)
        continue

    print(bfs(S, E))

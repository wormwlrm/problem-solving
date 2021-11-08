# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2023%20%EC%8B%A0%EA%B8%B0%ED%95%9C%20%EC%86%8C%EC%88%98

import sys
import math
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

primes = [2, 3, 5, 7]

queue = deque([2, 3, 5, 7])

digit = int(input())

depth = 0


def is_prime(n):
    root_square = math.ceil(int(n ** 0.5))

    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, root_square + 1, 2):
        if n % i == 0:
            return False

    return True


while queue:
    depth += 1

    if depth == digit:
        break

    for _ in range(len(queue)):
        n = queue.popleft()

        for i in [1, 3, 5, 7, 9]:
            appended = n * 10 + i

            if is_prime(appended):
                queue.append(appended)


print(*sorted(queue), sep='\n')

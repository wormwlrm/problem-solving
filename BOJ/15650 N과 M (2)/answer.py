import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

combos = list(combinations(range(1, N + 1), M))

for combo in combos:
    print(*combo)

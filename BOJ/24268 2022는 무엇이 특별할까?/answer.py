# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/24268%202022%EB%8A%94%20%EB%AC%B4%EC%97%87%EC%9D%B4%20%ED%8A%B9%EB%B3%84%ED%95%A0%EA%B9%8C%3F

import sys
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()


def convert(n, q):
    rev_base = ""

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


N, d = map(int, input().split())


target = int(convert(N, d))

combos = list(permutations(range(0, d), d))
combos = combos[len(combos) // d : :]
combos = [int("".join(list(map(str, i)))) for i in combos]

for i in combos:
    if i > target:
        print(int(str(i), d))
        exit()

print(-1)

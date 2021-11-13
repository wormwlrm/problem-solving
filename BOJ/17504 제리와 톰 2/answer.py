# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/17504%20%EC%A0%9C%EB%A6%AC%EC%99%80%20%ED%86%B0%202

import sys
import math

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

queue = list(map(int, input().split()))

ja = 1
mo = queue.pop()

while queue:
    next_mo = mo
    next_ja = queue.pop() * next_mo

    ja += next_ja
    mo = next_mo

    g = math.gcd(ja, mo)
    ja //= g
    mo //= g

    mo, ja = ja, mo

print(mo - ja, mo)

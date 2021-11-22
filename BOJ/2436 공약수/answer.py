# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2436%20%EA%B3%B5%EC%95%BD%EC%88%98

import sys
import math

input = lambda: sys.stdin.readline().rstrip()

GCD, LCM = map(int, input().split())

A_multiple_B = GCD * LCM

# 제곱수 있을 수도 있음
divisor = set([])

for i in range(1, math.ceil(math.sqrt(A_multiple_B)) + 1):
    if A_multiple_B % i == 0:
        divisor.add(i)
        divisor.add(A_multiple_B // i)

answer = [float('inf'), float('inf')]

for A in divisor:
    B = A_multiple_B // A

    if math.gcd(A, B) != GCD:
        continue

    if (A + B) < answer[0] + answer[1]:
        answer = [A, B]

print(*sorted(answer))
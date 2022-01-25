# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2166%20%EB%8B%A4%EA%B0%81%ED%98%95%EC%9D%98%20%EB%A9%B4%EC%A0%81

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
x, y = [], []
answer = 0

for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x, y = x + [x[0]], y + [y[0]]

for i in range(n):
    answer += (x[i] * y[i + 1]) - (x[i + 1] * y[i])

print(round(abs(answer) / 2, 1))

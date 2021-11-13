# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/14912%20%EC%88%AB%EC%9E%90%20%EB%B9%88%EB%8F%84%EC%88%98

import sys

input = lambda: sys.stdin.readline().rstrip()

N, d = map(int, (input().split()))

digit = {i: 0 for i in range(10)}

for i in range(1, N + 1):
    for j in str(i):
        digit[int(j)] += 1

print(digit[d])
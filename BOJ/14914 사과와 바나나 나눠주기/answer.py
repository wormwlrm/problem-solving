# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/14914%20%EC%82%AC%EA%B3%BC%EC%99%80%20%EB%B0%94%EB%82%98%EB%82%98%20%EB%82%98%EB%88%A0%EC%A3%BC%EA%B8%B0

import sys

input = lambda: sys.stdin.readline().rstrip()

B, A = map(int, input().split())

answers = []
for i in range(1, min(B, A) + 1):
    if (B % i == 0) and (A % i == 0):
        answers.append((i, B // i, A // i))

for answer in answers:
    print(answer[0], answer[1], answer[2])

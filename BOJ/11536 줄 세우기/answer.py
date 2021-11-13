# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/11536%20%EC%A4%84%20%EC%84%B8%EC%9A%B0%EA%B8%B0

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

man = []

for _ in range(N):
    man.append(input())

increased = sorted(man)
decreased = sorted(man, reverse=True)

if man == increased:
    print("INCREASING")
elif man == decreased:
    print("DECREASING")
else:
    print("NEITHER")

# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2693%20N%EB%B2%88%EC%A7%B8%20%ED%81%B0%20%EC%88%98

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    numbers = sorted(list(map(int, input().split())), reverse=True)
    print(numbers[2])
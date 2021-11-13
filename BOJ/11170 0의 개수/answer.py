# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/11170%200%EC%9D%98%20%EA%B0%9C%EC%88%98


import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    zero_count = 0

    start, end = map(int, input().split())

    for i in range(start, end + 1):
        for j in str(i):
            if j == '0':
                zero_count += 1

    print(zero_count)


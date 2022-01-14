# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/17362%20%EC%88%98%ED%95%99%EC%9D%80%20%EC%B2%B4%EC%9C%A1%EA%B3%BC%EB%AA%A9%20%EC%9E%85%EB%8B%88%EB%8B%A4%202

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

a = n % 8

if a in [1]:
    print(1)
elif a in [2, 0]:
    print(2)
elif a in [3, 7]:
    print(3)
elif a in [4, 6]:
    print(4)
elif a in [5]:
    print(5)

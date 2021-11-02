# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2845%20%ED%8C%8C%ED%8B%B0%EA%B0%80%20%EB%81%9D%EB%82%98%EA%B3%A0%20%EB%82%9C%20%EB%92%A4

import sys

input = lambda: sys.stdin.readline().rstrip()


a, b = map(int, input().split())
arr = list(map(int, input().split()))
answer = list(map(lambda x: x - a * b, arr))
print(*answer)

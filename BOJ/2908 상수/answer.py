import sys

input = sys.stdin.readline

N, M = map(str, input().split())


print(max(int(N[::-1]), int(M[::-1])))

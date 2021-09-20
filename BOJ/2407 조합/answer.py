import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ja = mo = 1

for i in range(1, M + 1):
    ja *= N
    mo *= i

    N -= 1

print(ja // mo)

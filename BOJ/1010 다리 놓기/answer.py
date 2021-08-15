import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    ja = 1
    for i in range(M, M - N, -1):
        ja *= i

    mo = 1
    for i in range(1, N + 1, 1):
        mo *= i

    print(ja // mo)

import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())


def fpow(under, n):
    if n == 1:
        return under

    half = fpow(under, n // 2) % C

    # 짝수면
    if n % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * under) % C


print(fpow(A, B) % C)

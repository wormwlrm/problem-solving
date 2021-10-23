# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/11444%20%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98%20%EC%88%98%206

import sys

input = lambda: sys.stdin.readline().rstrip()

divide = 1_000_000_007


class Matrix:
    def __init__(self, value=[[1, 1], [1, 0]]):
        self.value = value

    def __mul__(self, other):
        a = self.value
        b = other.value
        c = [[0, 0], [0, 0]]

        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c[i][j] += (a[i][k] * b[k][j]) % divide

        return Matrix(c)


base = Matrix()


def fpow(n):
    if n == 1:
        return base

    half = fpow(n // 2)

    # 짝수면
    if n % 2 == 0:
        return half * half
    else:
        return half * half * base


result = fpow(int(input()))

print(result.value[0][1] % divide)

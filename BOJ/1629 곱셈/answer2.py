import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())


def fpow(under, n):
    answer = 1

    while n:
        # n & 1 == 홀수
        if n & 1:
            answer *= under % C

        under *= under % C

        # 비트 오른쪽으로 한 칸 밈, n //= 2 와 같음
        n = n >> 1

    return answer


print(fpow(A, B) % C)

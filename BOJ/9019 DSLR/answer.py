import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def D(A):
    return (2 * A) % 10000


def S(A):
    return A - 1 if A != 0 else 9999


def L(A):
    d1 = A // 1000
    d2 = (A // 100) % 10
    d3 = (A // 10) % 10
    d4 = A % 10

    return d2 * 1000 + d3 * 100 + d4 * 10 + d1


def R(A):
    d1 = A // 1000
    d2 = (A // 100) % 10
    d3 = (A // 10) % 10
    d4 = A % 10

    return d4 * 1000 + d1 * 100 + d2 * 10 + d3


def solve(A, B):
    queue = deque([(A, '')])
    visited = [False] * 10001

    while True:
        value, stack = queue.popleft()

        # 이미 방문했으면
        if visited[value]:
            continue

        # 정답 발견하면
        if value == B:
            answer = "".join(stack)
            print(answer)
            break

        # 방문 표기
        visited[value] = True

        # D
        queue.append((D(value), stack + "D"))
        # S
        queue.append((S(value), stack + "S"))
        # L
        # L, R 반복 조심
        if len(stack) == 0 or stack[-1] != "R":
            queue.append((L(value), stack + "L"))
        # R
        # L, R 반복 조심
        if len(stack) == 0 or stack[-1] != "L":
            queue.append((R(value), stack + "R"))


for _ in range(T):
    A, B = map(int, input().split())

    solve(A, B)

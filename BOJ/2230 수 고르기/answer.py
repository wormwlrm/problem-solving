# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2230%20%EC%88%98%20%EA%B3%A0%EB%A5%B4%EA%B8%B0

import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

numbers = sorted([int(input()) for _ in range(N)])

left = 0
right = 0

answer = float("inf")

while left < N and right < N:
    # M과 같아지는 순간 더 찾아볼 필요 없이 종료
    if answer == M:
        print(answer)
        exit(0)

    current = numbers[right] - numbers[left]

    # M보다 같거나 크면
    if current >= M:
        answer = min(answer, current)
        left += 1

    # M보다 작으면
    else:
        right += 1

print(answer)

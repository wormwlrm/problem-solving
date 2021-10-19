# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/1806%20%EB%B6%80%EB%B6%84%ED%95%A9

import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

arr = list(map(int, input().split()))

left = 0
right = 0

acc = arr[0]

answer = float('inf')

while left < N:
    if (acc >= M):
        answer = min(answer, right - left + 1)
        acc -= arr[left]
        left += 1
    else:
        right += 1

        if (right >= N):
            break
        acc += arr[right]


print(answer if answer != float('inf') else 0)

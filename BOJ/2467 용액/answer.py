# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2467%20%EC%9A%A9%EC%95%A1

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

arr = list(map(int, input().split()))

left = 0
right = N - 1

answer = [float("inf"), float("inf")]
answer_sum = float("inf")


while left != right:
    sum = arr[left] + arr[right]

    if abs(sum) < abs(answer_sum):
        answer_sum = sum
        answer = [arr[left], arr[right]]

    if sum > 0:
        right -= 1
    else:
        left += 1


print(*answer)

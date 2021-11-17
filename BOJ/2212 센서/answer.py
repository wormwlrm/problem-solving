# https://github.com/wormwlrm/problem-solving/tree/master/BOJ/2212%20%EC%84%BC%EC%84%9C

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

K = int(input())

arr = sorted(list(map(int, input().split())))

# 간격 사이의 길이 배열, arr - 1만큼의 길이
queue = []

index = 1

while index < len(arr):
    heapq.heappush(queue, arr[index] - arr[index - 1])
    index += 1

answer = 0

while len(queue) >= K:
    distance = heapq.heappop(queue)
    answer += distance

print(answer)

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

numbers = input().strip()

stack = deque([])

delete_count = K

for i in range(N):
    while delete_count > 0 and stack and stack[-1] < numbers[i]:
        stack.pop()
        delete_count -= 1
    stack.append(numbers[i])

for _ in range(delete_count):
    stack.pop()

print("".join([*stack]))

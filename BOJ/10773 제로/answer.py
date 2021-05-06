import sys
from collections import deque

input = sys.stdin.readline

count = int(input())

stack = deque([])

for i in range(count):
    command = int(input())

    if (command == 0):
        stack.pop()
    else:
        stack.append(command)

answer = 0

while stack:
    answer += stack.pop()

print(answer)
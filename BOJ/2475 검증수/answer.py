import sys

input = sys.stdin.readline

numbers = map(int, input().split())

acc = 0

for number in numbers:
    acc += number ** 2

print(acc % 10)

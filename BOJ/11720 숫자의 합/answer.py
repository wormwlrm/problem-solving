import sys

input = sys.stdin.readline

N = int(input())

acc = 0

numbers = list(map(int, list(str(input().rstrip()))))

for number in numbers:
    acc += number

print(acc)

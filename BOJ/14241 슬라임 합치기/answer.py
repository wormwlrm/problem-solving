import sys

input = sys.stdin.readline

count = int(input())

numbers = list(map(int, input().split()))

acc = 0

for i in range(0, count - 1):
    for j in range(i + 1, count):
        acc += numbers[i] * numbers[j]

print(acc)

import sys

input = sys.stdin.readline

count = int(input())

numbers = list(map(float, input().split()))

sum = 0

max_num = max(numbers)

for i in numbers:
    sum += i / max_num * 100


print(sum / len(numbers))

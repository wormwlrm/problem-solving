import sys

input = sys.stdin.readline

N, X = map(int, input().split())

numbers = list(map(int, input().split()))

answer = []
for number in numbers:
    if number < X:
        answer.append(number)

print(*answer)

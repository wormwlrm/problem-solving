import sys

input = sys.stdin.readline

N = int(input())

numbers = list(range(1, N + 1))

acc = 1

zero_count = 0

divided_2 = 0

divided_5 = 0

for number in numbers:
    if number % 2 == 0:
        current = number

        while current % 2 == 0:
            divided_2 += 1
            current //= 2

    if number % 5 == 0:
        current = number

        while current % 5 == 0:
            divided_5 += 1
            current //= 5


print(min(divided_2, divided_5))

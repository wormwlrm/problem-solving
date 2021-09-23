import sys
import math

input = sys.stdin.readline

N = int(input())

numbers = []

for _ in range(N):
    numbers.append(int(input()))

numbers.sort()

real_gcd = numbers[1] - numbers[0]

index = 1

for i in range(2, N):
    real_gcd = math.gcd(real_gcd, numbers[i] - numbers[i - 1])


def get_divisor(n):
    divisor = set([])

    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor.add(i)
            divisor.add(n // i)

    return sorted(list(divisor))


divisor = get_divisor(real_gcd)
remove_1, *answer = divisor
print(*answer)

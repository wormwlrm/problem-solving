import math

count = int(input())

numbers = list(map(int, input().split()))

prime_count = 0

for i in numbers:
    if (i == 1):
        continue

    square_root = math.floor(i ** 0.5)

    is_prime = True

    for j in range(2, square_root + 1):
        if (i % j == 0):
            is_prime = False
            break

    if (is_prime == True):
        prime_count += 1

print(prime_count)

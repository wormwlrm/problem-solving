import math

first, last = (map(int, input().split()))

for i in range(first, last + 1):
    if (i == 1):
        continue

    square_root = math.floor(i ** 0.5)

    is_prime = True

    for j in range(2, square_root + 1):
        if (i % j == 0):
            is_prime = False
            break

    if (is_prime == True):
        print(i)

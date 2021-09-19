from math import ceil, sqrt


def is_prime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

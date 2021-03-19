a, b = map(int, input().split())


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def lcm(a, b):
    return a * b / gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))

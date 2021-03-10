import math

n, jimin, hansoo = map(int, input().split())

count = 1

while True:
    jimin = max(math.ceil(jimin / 2), 1)
    hansoo = max(math.ceil(hansoo / 2), 1)

    if (jimin == hansoo):
        break

    count += 1

print(count)

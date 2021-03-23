from math import ceil

up, down, height = (map(int, input().split()))

print(ceil((height - up) / (up - down)) + 1)

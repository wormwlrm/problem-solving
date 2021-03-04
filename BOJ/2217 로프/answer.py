count = int(input())
rest = []

for i in range(count):
    rest.append(int(input()))

rest.sort(reverse=True)

max = 0

for i in range(count):
    weight = rest[i] * (i + 1)
    if (weight > max):
        max = weight

print(max)
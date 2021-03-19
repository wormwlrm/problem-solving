n, m = map(int, input().split())

maximum = 0

for i in range(0, n - 1):
    for j in range(i, n):
        for k in range(j, n + 1):
            current = i + j + k
            if (current > maximum):
                maximum = current

print(maximum)

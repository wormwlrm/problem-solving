n, m = map(int, input().split())

cards = list(map(int, input().split()))

maximum = 0

for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            current = cards[i] + cards[j] + cards[k]
            if (current > maximum) and (current <= m):
                maximum = current

print(maximum)

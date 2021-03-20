n, k = map(int, input().split())

for i in range(1, k):
    n = n * (n - i)
    k = k * (k + 1)

print(n // k)

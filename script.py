n, k = map(int, input().split())

k = min(k, n - k)

if (k == 0):
    print(1)
else:

    b = n
    a = 1

    for i in range(1, k):
        b = b * (n - i)
        a = a * (i + 1)

    print(b // a)

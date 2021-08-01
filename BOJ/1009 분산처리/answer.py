import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    c = pow(a, b, 10)
    if c:
        print(c)
    else:
        print(10)

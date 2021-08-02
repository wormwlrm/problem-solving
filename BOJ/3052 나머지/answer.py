import sys

input = sys.stdin.readline

rest = set([])

for _ in range(10):
    rest.add(int(input()) % 42)

print(len(rest))

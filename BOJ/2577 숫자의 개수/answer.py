import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

multiply = str(A * B * C)

for c in range(10):
    print(multiply.count(str(c)))

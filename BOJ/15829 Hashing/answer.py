import sys

input = sys.stdin.readline

l = int(input().rstrip())
string = input().rstrip()

mod = 1234567891

acc = 0

powers = 1

for i in range(l):
    if (i != 0):
        powers = powers * 31 % mod
    acc += ((ord(string[i]) - 96) * powers) % mod

print(acc % mod)
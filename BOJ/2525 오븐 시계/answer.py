import sys

input = sys.stdin.readline

HH, MM = map(int, input().split())

ADD = int(input())

MM = MM + ADD

while MM >= 60:
    HH += 1
    MM -= 60

while HH >= 24:
    HH -= 24

print(str(HH) + " " + str(MM))

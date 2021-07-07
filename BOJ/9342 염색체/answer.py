import sys
import re

input = sys.stdin.readline

count = int(input())

for i in range(count):
    regex = re.compile('^[A-F]?A+F+C+[A-F]?$')
    dna = input().rstrip()
    if (regex.match(dna) == None):
        print("Good")
    else:
        print("Infected!")

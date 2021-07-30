import sys

input = sys.stdin.readline

string = input().rstrip().upper()

hash = {}

for char in range(65, 91):
    hash[chr(char)] = string.count(chr(char))

answer = ""
max = -1
for char in hash.keys():
    if hash[char] > max:
        max = hash[char]
        answer = char
    elif hash[char] == max:
        answer = "?"


print(answer)

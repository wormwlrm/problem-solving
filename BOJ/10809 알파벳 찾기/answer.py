import sys

input = sys.stdin.readline

string = input().rstrip()

answer = []

for char in range(97, 123):

    try:
        index = string.index(chr(char))
    except:
        index = -1

    answer.append(index)

print(*answer)

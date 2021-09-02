import enum
from re import split
import sys

input = sys.stdin.readline

chars = input().strip()


def parse(chars):
    arr = []
    acc = ""

    for char in list(chars):
        if char in ["+", "-"]:
            if acc != "":
                arr.append(int(acc))
            acc = ""

            arr.append(char)
        else:
            acc += char

    return arr + [int(acc)]


arr = parse(chars)

minus_exist = False

for index, value in enumerate(arr):
    # 짝수면 숫자임
    if index % 2 == 0:
        continue

    if value == "-":
        minus_exist = True

    if value == "+" and minus_exist == True:
        arr[index] = "-"

acc = 0
prev_sign = ""

for index, value in enumerate(arr):
    if index == 0:
        acc = value
        continue

    if value in ["+", "-"]:
        prev_sign = value
        continue

    if prev_sign == "-":
        acc = acc - value
    else:
        acc = acc + value

print(acc)

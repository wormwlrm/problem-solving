import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().split())

chars = sorted(list(input().strip().split()))

combos = list(combinations(list(range(C)), L))

answer = []


def contain_vowel(chars):
    for char in chars:
        if char in ["a", "e", "i", "o", "u"]:
            return True
    return False


def contain_two_consonant(chars):
    count = 0

    for char in chars:
        if char not in ["a", "e", "i", "o", "u"]:
            count += 1

            if count >= 2:
                return True

    return False


def is_valid(chars):
    if not contain_vowel(chars):
        return False

    if not contain_two_consonant(chars):
        return False

    return True


for combo in combos:
    temp = []

    for index in combo:
        temp.append(chars[index])

    if is_valid(temp):
        answer.append("".join(temp))

for case in sorted(answer):
    print(case)

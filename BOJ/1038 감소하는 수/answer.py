import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

numbers = list(range(9, -1, -1))

answers = []

for i in range(1, 11):
    combos = list(combinations(numbers, i))

    for combo in combos:
        temp = int("".join(list(map(str, list(combo)))))
        answers.append(temp)

answers.sort()

try:
    print(answers[int(input())])
except:
    print(-1)

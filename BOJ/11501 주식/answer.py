import sys

input = sys.stdin.readline

count = int(input())

for i in range(count):
    day = int(input())

    days = list(map(int, input().rstrip().split()))
    days.reverse()

    # 전체 이익
    profit = 0

    current_max = days[0]

    for j in days[1::]:
        if (j > current_max):
            current_max = j
        else:
            profit += current_max - j

    print(profit)

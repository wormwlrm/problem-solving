import sys

input = sys.stdin.readline


def is_valid(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def n_queen(x):
    global result

    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if is_valid(x):
                n_queen(x + 1)


N = int(input())
row = [0] * N
result = 0

n_queen(0)
print(result)

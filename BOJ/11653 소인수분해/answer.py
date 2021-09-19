import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    exit(0)


def prime_counter(N):
    counter = {}

    current = 2

    while N > 1:
        while N % current == 0:
            if current not in counter:
                counter[current] = 0

            counter[current] += 1
            N //= current

        current += 1

    return counter


counter = prime_counter(N)


for key in counter.keys():
    for value in range(counter[key]):
        print(key)

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

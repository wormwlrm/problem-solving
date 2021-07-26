import sys
import math

input = sys.stdin.readline

MAXIMUM = 1000001


def sieve_of_eratosthenes(end):
    prime_numbers = [True for _ in range(end + 1)]

    # 0과 1 제거
    prime_numbers[0] = False
    prime_numbers[1] = False

    for number in range(2, math.ceil(math.sqrt(end))):
        if prime_numbers[number] == True:
            # 해당 수 자체는 남겨두고 배수만 지움
            counter = 2
            while counter * number <= end:
                prime_numbers[counter * number] = False
                counter += 1

    return prime_numbers


prime_numbers = sieve_of_eratosthenes(MAXIMUM)

while True:
    command = int(input())

    if command == 0:
        break

    for index, value in enumerate(prime_numbers):
        if (value == True) and (prime_numbers[command - index] == True):
            print(str(command) + " = " + str(index) + " + " + str(command - index))
            break

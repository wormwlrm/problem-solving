import sys

input = sys.stdin.readline

T = int(input())


def D(left_index, right_index, direction, numbers):
    if direction == "left":
        left_index += 1
    else:
        right_index -= 1

    if left_index > right_index + 1:
        raise

    return (left_index, right_index)


def R(direction):
    if direction == "left":
        return "right"
    else:
        return "left"


for _ in range(T):
    commands = list(input().strip())

    number_counts = int(input())

    only_numbers = input().strip()[1:-1:]

    if len(only_numbers) > 0:
        numbers = list(map(int, only_numbers.split(",")))
    else:
        numbers = []

    left_index = 0
    right_index = len(numbers) - 1
    direction = "left"

    try:
        for command in commands:
            if command == "D":
                left_index, right_index = D(left_index, right_index, direction, numbers)
            elif command == "R":
                direction = R(direction)
    except:
        print("error")
        continue
    
    if (left_index > right_index):
        numbers = []
    else:
        numbers = list(map(str, numbers[left_index : right_index + 1 :]))

    if direction == "left":
        answer = "[" + ",".join(numbers) + "]"
    else:
        answer = "[" + ",".join(numbers[::-1]) + "]"

    print(answer)

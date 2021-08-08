import sys

input = sys.stdin.readline

K = int(input())

# Zero Padding
binary_tree = [0] + list(map(int, input().split()))

# Zero Padding
order_tree = list(range(len(binary_tree)))


def tree(current_index):
    try:
        current_value = order_tree[current_index]
    except IndexError:
        return []

    left_index = current_index * 2
    right_index = current_index * 2 + 1

    return tree(left_index) + [current_index] + tree(right_index)


order = tree(1)

answer = [[] for _ in range(K)]

for index, value in enumerate(order):
    depth = 0

    while True:
        if value // 2 == 0:
            break
        value //= 2
        depth += 1

    answer[depth].append(binary_tree[index + 1])

for level in answer:
    print(*level)

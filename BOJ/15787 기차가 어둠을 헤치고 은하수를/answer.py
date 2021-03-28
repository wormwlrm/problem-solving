train_count, command_count = map(int, input().split())

trains = [bin(0b0) for _ in range(train_count)]

for i in range(command_count):
    command = list(map(int, input().split()))
    train_index = command[1] - 1

    if command[0] == 1:
        seat_index = command[2] - 1

        trains[train_index] = bin(
            int(trains[train_index], 2) | (1 << seat_index)
        )
    elif command[0] == 2:
        seat_index = command[2] - 1

        trains[train_index] = bin(
            int(trains[train_index], 2) & ~(1 << seat_index)
        )
    elif command[0] == 3:
        trains[train_index] = bin(
            (int(trains[train_index], 2) << 1) & ~(1 << 20))
    elif command[0] == 4:
        trains[train_index] = bin((int(trains[train_index], 2) >> 1))

trains = set(list(map(lambda x: int(x, 2), trains)))

print(len(trains))

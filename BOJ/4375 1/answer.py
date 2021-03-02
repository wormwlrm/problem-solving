while True:
    try:
        x = int(input())
    except EOFError:
        break

    # 몇 번 반복되는지?
    count = 1

    # 현재 계산중인 값
    result = 1

    while True:

        if (result % x) == 0:
            print(count)
            break

        result = result * 10 + 1
        count += 1
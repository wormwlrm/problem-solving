while True:
    x = str(input())
    if (x == "0"):
        break

    mid = len(x) // 2
    index = 0

    while True:
        if (x[index] != x[-(index + 1)]):
            print('no')
            break
        elif (index == mid):
            print('yes')
            break
        index += 1

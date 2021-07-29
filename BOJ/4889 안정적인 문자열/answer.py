import sys

input = sys.stdin.readline


counter = 1

while True:
    string = list(input().rstrip())

    if string.count("-") > 1:
        break

    temp = string[::]
    count = 0
    while temp:
        promising_index = -1
        promising_weight = 3

        for i in range(1, len(temp)):
            if temp[i - 1] == "{":
                # ab 케이스
                if temp[i] == "}":
                    promising_weight = 0
                    promising_index = i
                    continue
                # aa 케이스는 가중치 있을 때만
                elif promising_weight >= 1:
                    promising_weight = 1
                    promising_index = i
            else:
                # bb 케이스도 가중치 더 작을 때만 갱신
                if temp[i] == "}" and promising_weight >= 1:
                    promising_weight = 1
                    promising_index = i
                # ba 케이스
                elif promising_weight >= 2:
                    promising_weight = 2
                    promising_index = i

        temp = temp[0 : promising_index - 1 :] + temp[promising_index + 1 : :]

        count += promising_weight

    print(str(counter) + ". " + str(count))
    counter += 1

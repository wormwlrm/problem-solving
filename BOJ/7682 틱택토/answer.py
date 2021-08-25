import sys

input = sys.stdin.readline


def is_bingo(b1, b2, b3, t):
    if b1 == t and b2 == t and b3 == t:
        return True


def get_bingo_cases(b):
    # 가로 세 줄
    cases = [[b[j][i] for i in range(3)] for j in range(3)]
    # 세로 세 줄
    cases += [[b[i][j] for i in range(3)] for j in range(3)]
    # \ 대각선 한 줄
    cases += [[b[0][0], b[1][1], b[2][2]]]
    # / 대각선 한 줄
    cases += [[b[0][2], b[1][1], b[2][0]]]

    return cases


def empty_exist(b):
    for y in range(3):
        for x in range(3):
            if b[y][x] == ".":
                return True
    return False


def get_bingo_state(cases):
    o_bingos = []
    x_bingos = []

    index = 0

    for case in cases:
        c1 = case[0]
        c2 = case[1]
        c3 = case[2]
        if is_bingo(c1, c2, c3, "O"):
            o_bingos.append(index)
        elif is_bingo(c1, c2, c3, "X"):
            x_bingos.append(index)
        index += 1

    return [o_bingos, x_bingos]


while True:
    case = input().strip()

    if case == "end":
        break

    board = [list(case[:3:]), list(case[3:6:]), list(case[6:9:])]

    x_count = case.count("X")
    o_count = case.count("O")

    try:
        cases = get_bingo_cases(board)

        o_bingos, x_bingos = get_bingo_state(cases)

        # O 승리
        # O 빙고 완성, X 빙고 미완성, O는 X와 숫자가 같아야 함
        if len(o_bingos) > 0 and len(x_bingos) == 0 and x_count == o_count:
            print("valid")
            continue

        # X 승리
        # X 빙고 완성, O 빙고 미완성, X는 O보다 1 많아야 함
        if len(x_bingos) > 0 and len(o_bingos) == 0 and x_count == o_count + 1:
            print("valid")
            continue

        # 비김
        # X 빙고 없음, O빙고 없음, 게임판 가득 찬 경우
        if (
            len(x_bingos) == 0
            and len(o_bingos) == 0
            and not empty_exist(board)
            and x_count == 5
            and o_count == 4
        ):
            print("valid")
            continue

        raise
    except:
        print("invalid")

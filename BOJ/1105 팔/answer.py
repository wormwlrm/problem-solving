import sys

input = sys.stdin.readline

L, R = input().rstrip().split()


def contains_8(string: str):
    try:
        return string.index("8") >= 0 and True
    except:
        return False


# L, R 중 하나라도 8이 없는 경우
if not contains_8(L) or not contains_8(R):
    print(0)
# L, R의 자릿수가 다른 경우
elif len(L) != len(R):
    print(0)
# L, R이 같은 경우
elif L == R:
    print(L.count("8"))
# L, R이 다른 경우
else:
    acc = 0

    for index in range(len(R)):
        if L[index] == R[index] and L[index] == "8":
            acc += 1
        # 앞에서부터 탐색하다가 서로 다른 숫자를 만나면 거기서 끝! 뒷자리는 알 바 아님!
        # 8이 포함되어 있던 없던 8 피해서 선택하면 됨
        elif L[index] != R[index]:
            break

    print(acc)

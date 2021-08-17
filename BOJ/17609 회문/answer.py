import sys

input = sys.stdin.readline

N = int(input())


def is_palindrom(string: str) -> bool:
    return string == "".join(reversed(string))


for i in range(N):
    string = input().strip()

    if is_palindrom(string):
        print(0)
        continue

    # 2개면 그냥 유사 회문
    if len(string) == 2:
        print(1)
        continue

    index = 0
    # 3개부터는 판단
    while True:
        front_index = index
        back_index = len(string) - index - 1

        # 같으면 그냥 날림
        if string[front_index] == string[back_index]:
            index += 1
            continue

        # 다르면 front를 뺀 게 팰린드롬인지, back을 뺀게 팰린드롬인지 판단
        if is_palindrom(
            "".join(string[front_index + 1 : back_index + 1 :])
        ) or is_palindrom("".join(string[front_index:back_index:])):
            print(1)
            break
        else:
            print(2)
            break

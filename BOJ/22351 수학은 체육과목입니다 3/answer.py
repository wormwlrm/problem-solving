import sys

input = sys.stdin.readline

number = str(input().rstrip())

minimum = 0
maximum = 999

digit = 1

while digit <= 3:
    # 다음 숫자를 [cursor: cursor + current+digit : ]로 구한다
    cursor = 0
    current_digit = digit

    # 최솟값으로 쓰기 위해 시작 숫자 저장
    current_min = -1

    # 직전 숫자
    last_saved_number = -1

    # 파싱 성공 여부
    parsed = True

    while parsed and cursor < len(number):
        current_item = int("".join(number[cursor : cursor + current_digit :]))
        expected_item = last_saved_number + 1

        if last_saved_number == -1:
            last_saved_number = current_item
            current_min = last_saved_number
        elif current_item != expected_item:
            parsed = False
            continue
        else:
            last_saved_number = current_item

        # 자릿수 올려야 하는 경우
        if current_item in [9, 99, 999]:
            cursor += current_digit
            current_digit += 1
        else:
            cursor += current_digit

    if parsed:
        maximum = current_item
        minimum = current_min
        break

    digit += 1

print(minimum, maximum)

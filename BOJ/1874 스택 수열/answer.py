count = int(input())

expected_input = [i for i in range(1, count + 1)]

real_output = []

answer = []

valid = True

cursor = 1

for _ in range(count):
    current = int(input())

    # 크거나 같으면 일단 스택에 더하기
    while (cursor <= current):
        real_output.append(cursor)
        answer.append('+')
        cursor += 1

    if (real_output[-1] == current):
        real_output.pop()
        answer.append('-')
    else:
        valid = False

if (valid):
    print(*answer, sep="\n")
else:
    print("NO")

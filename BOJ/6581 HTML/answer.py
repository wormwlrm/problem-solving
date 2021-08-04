import sys

# input = sys.stdin.readline

words = []

while True:
    try:
        words.extend(map(str, input().rstrip().split()))
    except:
        break

max_length = 80


def get_total_length_of_current_line(current_line):
    acc = 0
    for word in current_line:
        acc += len(word)

    whitespace = len(current_line)

    return acc + whitespace


output = []

current_line = []

for word in words:
    if word == "<br>":
        # 줄 플러시
        output.append(current_line[::])
        current_line.clear()
        continue
    elif word == "<hr>":
        # 줄 플러시
        if len(current_line) > 0:
            output.append(current_line[::])
        # 줄 추가
        output.append(["-" * max_length])
        current_line.clear()
        continue

    if get_total_length_of_current_line(current_line) + len(word) <= max_length:
        current_line.append(word)
    else:
        output.append(current_line[::])
        current_line.clear()
        current_line.append(word)

if len(current_line) > 0:
    output.append(current_line)

for line in output:
    print(*line)

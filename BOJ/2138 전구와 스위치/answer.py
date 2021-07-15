import sys

input = sys.stdin.readline

count = int(input())

start = str(input().rstrip())
end = str(input().rstrip())


def toggle(status):
    if status == "0":
        return "1"
    else:
        return "0"


def toggled(status, index):
    if index == 0:
        str1 = toggle(status[index])
        str2 = toggle(status[index + 1])

        return str1 + str2 + status[2::]
    elif index == len(status) - 1:
        str1 = toggle(status[index - 1])
        str2 = toggle(status[index])

        return status[:-2:] + str1 + str2
    else:
        str1 = toggle(status[index - 1])
        str2 = toggle(status[index])
        str3 = toggle(status[index + 1])

        return status[: index - 1 :] + str1 + str2 + str3 + status[index + 2 : :]


def calculate(first_on: bool):
    current = start

    toggled_count = 0
    start_index = 1

    if first_on:
        toggled_count += 1
        current = toggled(current, 0)

    for i in range(start_index, count):
        if current[i - 1] == end[i - 1]:
            continue
        else:
            current = toggled(current, i)
            toggled_count += 1

    if current == end:
        return toggled_count
    else:
        return -1


on = calculate(True)
off = calculate(False)

if on == -1 and off == -1:
    print(-1)
elif on == -1 and off > -1:
    print(off)
elif on > -1 and off == -1:
    print(on)
else:
    print(min(on, off))

import sys

input = sys.stdin.readline

start, end, finish = map(str, input().split())

logs = {}

checked = []

while True:
    try:
        timestamp, name = map(str, input().split())
    except:
        break

    if timestamp <= start:
        logs[name] = True
    elif end <= timestamp <= finish:
        if name in logs and logs[name] == True:
            checked.append(name)
            logs[name] = False

print(len(checked))

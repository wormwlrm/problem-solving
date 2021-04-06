n = int(input())


current = 666
answer = []

while len(answer) < n:
    if (str(current).find('666') >= 0):
        answer.append(current)
    current += 1

print(answer[-1])

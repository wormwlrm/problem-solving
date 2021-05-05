number = int(input())

bunehap = number

answer = 0

while bunehap:
    stringified = list(map(int, list(str(bunehap))))

    current = bunehap
    for i in stringified:
        current += i

    if (current == number):
        answer = bunehap

    bunehap -= 1

print(answer)
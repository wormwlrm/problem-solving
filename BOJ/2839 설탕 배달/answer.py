total = int(input())

answer = 0

three_count = 0

while total >= 0:
    value = total // 5
    left = total % 5

    if (left == 0):
        answer = value + three_count
        break
    else:
        three_count += 1
        total -= 3

if (total < 0):
    print(-1)
else:
    print(answer)


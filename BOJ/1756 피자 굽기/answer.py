depth, pizza_count = map(int, input().split())

oven = list(map(int, input().split()))

pizza = list(map(int, input().split()))

acceptable = [oven[0]]

for i in range(1, depth):
    acceptable.append(min(oven[i], acceptable[i - 1]))

answer = depth - 1
max_radius = 0

full = False

for current_pizza in pizza:
    # 작거나 같아서 그냥 쌓아지면 right만 줄이기
    if (current_pizza <= max_radius):
        answer = answer - 1
    else:
        left = 0
        right = answer

        while left <= right:
            mid = (left + right) // 2
            temp_pizza = acceptable[mid]

            if (temp_pizza < current_pizza):
                right = mid - 1
            elif (temp_pizza > current_pizza):
                left = mid + 1
            else:
                left = mid + 1

        answer = right

    # 넣을 인덱스가 없는 경우
    if (answer < 0):
        full = True
        break

    max_radius = acceptable[answer]

if full:
    print(0)
else:
    print(answer + 1)

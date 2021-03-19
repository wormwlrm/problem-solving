from collections import deque

count = int(input())

for i in range(count):
    string = list(str(input()))
    stack = deque([])

    for j in string:
        stack.append(j)

        if (len(stack) >= 2 and stack[-2] == "(" and stack[-1] == ")"):
            stack.pop()
            stack.pop()

    print('NO') if len(stack) > 0 else print('YES')

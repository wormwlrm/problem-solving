import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input())

for i in range(testcase):
    doc_count, index = map(int, input().split())
    
    docs = deque()
    arr = list(map(int, input().split()))
    for i, value in enumerate(arr):
        docs.append((value, True if i == index else False))

    print_count = 0

    while docs:
        current = docs.popleft()

        most_priority = True

        for i in docs:
            if (i[0] > current[0]):
                most_priority = False
        
        if (most_priority):
            print_count += 1

            if (current[1]):
                print(print_count)
                break
        else:
            docs.append(current)

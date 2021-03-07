k, n = map(int, input().split())
lengths = [int(input()) for _ in range(k)]

right = max(lengths)
left = 1

maxLength = 0

while left <= right:
    mid = (right + left) // 2
    
    value = 0
    for cur in lengths:
        value += cur // mid


    if (value == n):
        left = mid + 1
        maxLength = mid
    elif (value > n):
        left = mid + 1
        maxLength = mid
    else:
        right = mid - 1

print(maxLength)
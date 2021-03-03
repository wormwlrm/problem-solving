import sys
desk, man = map(int, input().split())
times = [int(input()) for _ in range(desk)]

maximum = max(times)

minTime = 1
maxTime = maximum * man

while minTime <= maxTime:
    mid = ((maxTime + minTime) // 2)

    value = 0
    for cur in times:
        value += mid // cur

    if value >= man:
        maxTime = mid - 1
        result = mid
    else:
        minTime = mid + 1

print(minTime)
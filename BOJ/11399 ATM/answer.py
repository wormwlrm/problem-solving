count = int(input())

times = list(map(int, input().split()))

times.sort()

result = 0
acc = 0
cur = times[0]

for i in range(len(times)):
    cur = times[i]
    acc += cur
    result += acc

print(result)

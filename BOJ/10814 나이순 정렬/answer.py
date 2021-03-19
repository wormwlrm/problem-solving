count = int(input())

arr = []

for i in range(count):
    age, name = input().split()
    age = int(age)
    arr.append((age, name, i))

arr.sort(key=lambda x: (x[0], x[2]))

for i in arr:
    print(str(i[0]) + ' ' + i[1])

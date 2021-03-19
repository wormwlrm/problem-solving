case = int(input())

for i in range(case):
    h, w, n = map(int, input().split())

    floor = ((n - 1) % h) + 1
    room = ((n - 1) // h) + 1

    print(str(floor) + str(room).zfill(2))

import sys

input = sys.stdin.readline

max_length = 20

# zero padding
binary = bin(0x0)

count = int(input().rstrip())

for i in range(count):
    token = input().rstrip().split()

    if (len(token) == 1):
        command = token[0]
    else:
        command = token[0]
        arg = int(token[1])

    if (command == 'add'):
        # arg 번째 숫자를 1로 만듦
        binary = bin(int(binary, 2) | (1 << (arg - 1)))
    elif (command == 'remove'):
        # arg 번째 숫자를 0으로 만듦
        binary = bin(int(binary, 2) & ~(1 << (arg - 1)))
    elif (command == 'check'):
        # 있으면 1, 없으면 0 출력
        print(1 if bin(int(binary, 2) & (1 << (arg - 1))) > bin(0x0) else 0)
    elif (command == 'toggle'):
        # 특정 인덱스 XOR
        binary = bin(int(binary, 2) ^ (1 << (arg - 1)))
    elif (command == 'all'):
        binary = bin(0b11111111111111111111)
    elif (command == 'empty'):
        binary = bin(0b0)

string = input().split()

n = int(string[0])
b = str(bin(int(string[1])))[2:]

mod = 1000


# 최대 입력값 100000000000을 이진수로 자리 바꿨을 때 37자리로 나옴
squares = [None for _ in range(38)]

# 처음에 입력된 매트릭스
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        matrix[i][j] = row[j]

squares[0] = matrix

# 정답 매트릭스 초기화
answer = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    answer[i][i] = 1


# 매트릭스 곱 함수
def multiply(a, b):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = (
                    result[i][j] + ((a[i][k] * b[k][j]) % mod)) % mod

    return result


for i in range(1, len(b) + 1):
    squares[i] = multiply(squares[i - 1], squares[i - 1])

for i in range(len(b)):
    if (b[-(i+1)] == '0'):
        continue
    answer = multiply(answer, squares[i])

for row in answer:
    print(*row)

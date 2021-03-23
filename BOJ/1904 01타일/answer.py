index = int(input())

fibonacci = {1: 1, 2: 2}

for i in range(3, index + 1):
    fibonacci[i] = (fibonacci[i - 2] + fibonacci[i - 1]) % 15746

print(fibonacci[index])

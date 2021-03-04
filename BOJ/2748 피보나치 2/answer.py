index = int(input())

fibonacci = {0: 0, 1: 1}

def recursive(i):
    current = 0

    if i > len(fibonacci) - 1:
        current = None
    else:
        current = fibonacci[i]

    if current != None:
        return fibonacci[i]
    else:
        fibonacci[i] = recursive(i - 1) + recursive(i - 2)
        return fibonacci[i]

print(recursive(index))
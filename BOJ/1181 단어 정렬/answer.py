count = int(input())

words = {}

for i in range(count):

    x = str(input())
    length = len(x)
    if (length not in words):
        words[length] = set([])

    words[length].add(x)

words = sorted(words.items())

for _i, i in words:
    for j in sorted(list(i)):
        print(j)

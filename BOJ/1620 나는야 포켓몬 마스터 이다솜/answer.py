import sys

input = sys.stdin.readline

dictionary_count, quiz_count = map(int, input().split())

pokemon_name = {}

pokemon_number = {}

for i in range(1, dictionary_count + 1):
    name = str(input().rstrip())

    pokemon_number[i] = name
    pokemon_name[name] = i

for i in range(quiz_count):
    quiz = str(input().rstrip())

    if (quiz.isdigit()):
        print(pokemon_number[int(quiz)])
    else:
        print(pokemon_name[quiz])


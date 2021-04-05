people_count, party_count = map(int, input().split())

truth_count, *truth = map(int, input().split())

# zero-padding
parent = [i for i in range(people_count + 1)]

parties = []


def find(x):
    if x == parent[x]:
        return x

    # 부모 거를 자식에 넣음
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    '''
    x와 y를 연결, 노드 숫자 작은 거를 부모로
    '''
    x_root = find(x)
    y_root = find(y)

    if (x_root == y_root):
        return

    if (x_root < y_root):
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


for current_party in range(party_count):
    current_people_count, *participants = map(int, input().split())
    participants = sorted(participants)

    parties.append(participants)
    representative = participants[0]

    for participant in participants:
        if (find(representative) == find(participant)):
            continue
        else:
            union(representative, participant)

parasited = set([])

for truther in truth:
    for idx in range(1, people_count + 1):
        if (find(idx) == find(truther)):
            parasited.add(idx)

answer = 0

for current_party in parties:
    origin = len(set(current_party))
    subtracted = origin - len(set(current_party) - parasited)
    if (origin - subtracted == origin):
        answer += 1

print(answer)

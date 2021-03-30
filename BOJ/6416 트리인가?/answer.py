case = 1

# -1, -1 이 올 때까지 테스트 진행
testing = True

while testing:
    # 기본적으로 Tree
    is_tree = True

    # 0, 0이 올 때까지 테스트 진행
    current_case = True

    # 부모 자식 관계
    parent = {}

    while current_case:
        row = list(map(int, input().split()))

        for i in range(len(row) // 2):
            u = row[i * 2]
            v = row[i * 2 + 1]

            # 전체 테스트 종료
            if (u == -1 and v == -1):
                current_case = False
                testing = False
                continue

            # 테스트 케이스 입력 입력 종료
            if (u == 0 and v == 0):
                current_case = False
                continue

            # 부모 노드도 넣기
            if (u not in parent):
                parent[u] = None

            # 자식 노드
            if (v not in parent) or (parent[v] == None):
                parent[v] = u
            else:
                # 부모가 둘이라는 뜻
                is_tree = False
                break

    if not testing:
        break

    # parent 가 비어있으면 스킵
    if is_tree == True and bool(parent):

        root_count = 0
        # 부모 없는 노드가 단 하나인지 확인
        for i in parent:
            if parent[i] is None:
                root_count += 1
                continue

        if (root_count != 1):
            is_tree = False

    if (is_tree):
        print('Case ' + str(case) + ' is a tree.')
    else:
        print('Case ' + str(case) + ' is not a tree.')

    case += 1

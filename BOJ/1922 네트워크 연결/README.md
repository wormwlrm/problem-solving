## 1922 네트워크 연결

<https://www.acmicpc.net/problem/1922>

## 내가 생각한 방법

- 최소 신장 트리 문제
  - 정점의 수는 1000개, 간선의 수는 100000개까지 가능
  - 프림이 좀 더 효율적인 것 같지만 일단 크루스칼로 풀어보자
- 크루스칼을 쓰려면 `find`와 `union` 을 미리 구현해야 한다
  - 각 노드의 부모를 나타내는 배열을 선언한다
    - 이 때 초기값은 자기자신을 가리키도록 해서 모든 노드가 연결되지 않은 상태를 유지
  - `find`는 트리의 루트를 반환
  - `union`은 한 쪽 트리의 루트를 다른 쪽에다가 연결
- 가중치를 기준으로 엣지들을 정렬하고, `parent`를 바꿔가면서 붙여나간다
  - 가중치만 알면 되니까 엣지 갯수가 처음 입력한 값과 같다면 더 이상 `parent` 갱신할 필요 없이 `break`
  - 부모가 같다면 사이클 발생하니 잇지 않기

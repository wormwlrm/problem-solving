## 2644 촌수 계산

<https://www.acmicpc.net/problem/2644>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- 출발지와 목적지가 명확하므로 다익스트라를 써보자
  - <https://justkode.kr/algorithm/python-dijkstra>
- 다익스트라 알고리즘 짜는 법은 좀 상기시켜 둘 필요가 있을 듯.
  - 우선 입력을 이용해 간선으로 그래프를 구성함
  - 다익스트라는 그래프, 첫 번째 노드를 파라미터로 받음
  - 현재 노드에서 다른 노드까지의 거리를 딕셔너리로 만듦
  - 우선순위 큐를 쓰는데 튜플을 활용
    - 이때 정렬 기준은 거리임
    - `current_cost` 는 현재 노드까지 도달하는데 걸린 비용
    - `current_node` 는 현재 노드
  - 인접 노드들에 대해 `distances`랑 `current_cost + graph[current_node][adjust_node]` 를 비교
  - 짧은 것으로 갱신하고 우선순위 큐에 다시 집어넣기

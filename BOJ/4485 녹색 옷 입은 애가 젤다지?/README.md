## 4485 녹색 옷 입은 애가 젤다지?

<https://www.acmicpc.net/problem/4485>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- DP + BFS + 우선순위 큐 (사실 상 다익스트라)
  - DP 배열에는 특정 지점까지 도달하는데 걸리는 최소 비용을 저장
  - BFS로 네 방향 탐색하되, 비용이 적을 때만 큐에 넣음
  - 큐는 우선순위 큐로 만들어서 최종점에 도착하는 순간 탈출
  - 마지막에 `count += 1` 빠트려서 시간 낭비함 ㅋㅋ

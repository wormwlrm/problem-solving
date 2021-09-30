## 13023 ABCDE

<https://www.acmicpc.net/problem/13023>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- DFS라고 생각했는데 맞음
- 시간 초과가 떴는데 다음 방법으로 좀 낮춤
  - 뎁스를 상수로 넘겨줆으로써 `visited.count(True)` 를 대체함
  - graph는 전역 변수로
  - 루프 탈출하는 데 걸리는 시간 줄이기 위해 뎁스 5 되는 즉시 1 출력하고 종료

## 2531 회전 초밥

<https://www.acmicpc.net/problem/2531>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- 투 포인터라고 하는데 굳이...? 그냥 원형 큐 인덱스 조건만 잘 알고 있으면 그냥 풀 수 있는 듯 하다.
- 근데 파이썬에서는 시간 초과가 따서 PyPy로 성공함
  - N번째 인덱스부터 N+K번째 인덱스까지 초밥 탐색
  - 쿠폰이 있기 때문에 C는 항상 1로 만들고 시작
  - 중복 제거 위해 `set` 배열 인덱스를 써서 시간을 줄여보자
- 슬라이딩 윈도우 방법으로도 풀어보았다
  - 특정 범위를 커서로 잡고 그 사이에 있는 종류들을 미리 구해놓은 뒤,
  - 커서를 오른쪽으로 한 칸씩 당기면서 빠지는 것과 추가되는 것을 매번 계산하면 됨
  - 그러면 `O(n)`으로 된다는 말이 맞다

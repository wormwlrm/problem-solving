## 2805 나무 자르기

<https://www.acmicpc.net/problem/2805>

## 내가 생각한 방법

- 딱 보니 이분탐색인게 티가 나더라
- `left`를 0, `right`를 최대 나무 높이로 설정한 후 이분탐색함
- 값이 모자란 경우는 허용이 안되기 때문에 값이 넘치는 경우에만 `answer`를 `mid`로 해줌
- 근데 시간 오버되어서 PyPy로 풂

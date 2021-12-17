## 2230 수 고르기

<https://www.acmicpc.net/problem/2230>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- 정렬 및 투포인터로 컷
  - left, right 포인터를 둔다
    - 두 값은 모두 0으로 설정
    - 같은 값을 가리킬 수도 있다고 문제에 정의됨
  - `numbers[right] - numbers[left]`가 M보다 같거나 크면 `answer` 갱신하기
  - 작으면 `right` 늘려서 값의 차이 증가시키기

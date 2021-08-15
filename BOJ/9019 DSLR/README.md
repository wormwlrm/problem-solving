## 9019 DSLR

<https://www.acmicpc.net/problem/9019>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- 백트래킹으로 보임
  - 그래서 DFS로 풀었음
- 근데 시간이랑 메모리에 굉장히 예민하네...

  - 재방문하지 않게 `visited` 배열 관리 필요
  - `L, R`은 반복되지 않게 전처리 해주면 2초 정도 시간이 줄어들긴 하는 듯

    ```python
    if len(stack) == 0 or stack[-1] != "R":
    ```

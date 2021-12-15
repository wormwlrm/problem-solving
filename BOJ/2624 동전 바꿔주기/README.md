## 2624 동전 바꿔주기

<https://www.acmicpc.net/problem/2624>

## 내가 생각한 방법

<!-- ![이미지](./img.png) -->

- DP인데 갯수 DP라서 헷갈림 주의
  - 어려워서 답 봄ㅠ

```python
for coin_value, coin_count in money: # 코인 값, 코인 갯수
    for current_money in range(T, 1, -1): # 현재 가리키고 있는 값을 뒤에서부터 읽기
        for current_count in range(1, coin_count + 1): # 코인 갯수 적용하기
            if current_money - current_count * coin_value >= 0: # 만약 현재 값 - 코인 갯수 뺀 게 유효하다면 DP 적용
```

![image](./Untitled.png)
1. 시간 초과.
    ```python
    def solution(weights:list)->int:
        ans = []
        for i,v in enumerate(weights):
            if v in weights[i+1:]:
                ans.append((v,v))
            if v*2 in weights[i+1:]:
                ans.append((v,v*2))
            if v*3%2 == 0 and v*3/2 in weights:
                ans.append((v,v*3/2))
            if v*4%3 == 0 and v*4/3 in weights:
                ans.append((v,v*4/3))
        return len(ans)
    ```
- 리스트에서 찾는게 시간이 많이 먹어서, O(n^2) 이내에서 처리해야합니다.
    - `v*4/3 in weights` 이렇게 weights 리스트 내에서 값을 찾을 때 시간을 많이 먹음.
    - 조건에서도 10만 제한
- set 을 사용해서 빨리 찾아서 연산하도록 한다.
- Counter를 쓰되, 정수일 때만 계산하도록 작성


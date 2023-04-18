### 접근방법

1. list를 이용한 `push` , `pop` 을 이용. (정답 X)
    
    ```python
    def solution(seq:list, k:int)->list:
        ans = []
        answer = []
        sum = 0
        minimum = len(seq)
        if k in seq :
            return [seq.index(k),seq.index(k)]
        for i,v in reversed(list(enumerate(seq))):
            sum += v
            ans.append(i)
            while sum >= k :
                if sum == k and ans[0] - ans[-1] <= minimum:
                    minimum = ans[0] - ans[-1]
                    answer = [ans[-1],ans[0]]
                sum -= seq[ans.pop(0)]
        return answer
    ```
    
2. two pointers 접근 (정답 O)
    
    ```python
    def solution(seq:list, k:int)->list:
        answer = []
        sum = 0
        left = 0
        _len = len(seq)
        minimum = len(seq)
        if k in seq :+
            return [seq.index(k),seq.index(k)]
        seq.reverse()
        for i,v in enumerate(seq):
            right = i
            sum += v
            if sum >= k :
                if sum == k and right - left <= minimum:
                    minimum = right - left
                    answer = [ _len-1-right,_len-1-left]
                sum -= seq[left]
                left += 1
        return answer
    ```
    

## 학습내용

<aside>
💡 첫풀이에서 시간초과 에러가 떴으며, 로직상 문제는 없으나 O(n)으로 줄여야 할 것이라고 판단.
    → 5 ≤ `sequence`의 길이 ≤ 1,000,000 → 100만 기준 1번의 for문.
`seq` 가 비내림차순으로 정렬되었으며, while문을 지울 수 있을거라 생각이 들었습니다.

</aside>

- list를 이용한 풀이 방법이나, 2 pointers 나 큰 문제는 되지 않았을거라 생각합니다.
- 다만, 비내림차순임을 인식하고 단 한번의 for문으로 while을 어떻게 없앨 수 있을지 빠르게 판단할 수 있어야 합니다.
→ `reverse` 로 정렬 시킨 리스트는 마지막을 빼는게 더하는것보다 늘 크기 때문에, 반복해서 리스트의 `leftpop` 할 필요가 없습니다.
- 그 후 결과값을 인덱싱하여 리턴하도록 하였습니다.
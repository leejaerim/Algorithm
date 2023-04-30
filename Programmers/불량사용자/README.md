## 불량사용자 

### 접근(구분하여 접근)
1. `user_id`에서 `banned_id`에 해당 되는지 체크
2. 어떻게 아이디를 바인딩 할것인지 알고리즘 구현
   1. **_순열, 그리고 조합을 계산해야됨. = `combination, permutation`_**
     2. 특정 값을 골랐을 경우, 후에 선택에 영향을 미치는 종속적 순열 = **_백트래킹 DFS 필요._**
3. 중복값을 어떻게 제거할 것인가 학인 = `set`
### 학습내용
> **핵심은 어떻게 중복을 제거할 것인가** 
- `_set[i] = (_set[i][0]+1, _set[i][1])`
    k값을 증가시켜 자료구조 set에 저장하는 풀이
- `def dfs(keys:list,index:int, ans:list, _set:set,target:list)` dfs 구현 (while로도 구현할 줄 알아야 함.)
- `from itertools.combination(Iterable,number)` 조합
- **_divide & conquer_** = 문제를 분할해서 바라보고 필요한 알고리즘을 구현하였다.
### 오래 걸렸던 부분

 - `user_id와 banned_id`가 `['ab','bb','cb'], ['*b','**']` 일 때, `target`의 타입이
    `list`로 `['ab','bb'], ['bb','ab']`가 중복제거 없이 삽입되었음.
 - `target` 자료구조를 `set`으로 두어, 중복제거
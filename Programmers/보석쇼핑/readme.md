- 접근방향
    - set사용해서 gems의 check를 직접 확인
    - dequeue? left, right 를 사용해서 2포인트 접근?
    - 처음 list 는 모든 값들을 가지고 있을 것이므로, 모든 list값에서 
    gems_check를 다 가질 수 있는 한에서 좌측값 빼고 우측값 빼서 최소값 도출
    
    ```python
    def solution(gems:list)-> list:
        temp = list(gems)
        target = len(list(set(gems)))
    
        left = 0
        ans = []
        right = len(gems)
        # 왼쪽 부터
        while target == len(list(set(temp))):
            left += 1
            item = temp.pop(0)
        temp.append(item)
    
        while target == len(list(set(temp))):
            right -= 1
            item = temp.pop(right - left)
        ans.append((right+1 - left, [left, right+1]))
    
        left = 0
        right = len(gems)
        temp = list(gems)
        # #오른쪽
        while target == len(list(set(temp))):
            right -= 1
            item = temp.pop(right)
        temp.append(item)
        while target == len(list(set(temp))):
            left += 1
            item = temp.pop(0)
        ans.append((right+1-left, [left, right + 1 ]))
        a, a_list = ans.pop()
        b, b_list = ans.pop()
        if a > b :
            return b_list
        else :
            return a_list
    ```
    
    - `["A", "AA", "AA", "AAA", "AA", "A"]`
    - 위와 같은 테스트 케이스에서 좌측 혹은 먼저 우측 먼저 하느냐에 따라 값이 다름.
    - while문을 좌/우측 두번으로 나누어서 최소값으로 제공
    - ***단일 while문임에도 불구 list(set(temp)) 만드는 시간복잡도가 초과***
- 다른 방향으로 접근
    - dictionary 사용해서 키 밸류 존재하는지 체크하도록 함(이전 코드에서의 target과 동일)
    - 10만 이기에 1번의 반복만 가능하되, 조건부 while 가능.
        - 모든 값들이 1번씩 존재할때만 while 통해서 왼쪽을 지운다.
        - left는 단방향 진행해야 된다.
    - heap 트리 사용하여 최소값 반환하여 리턴
    - ***단, (-)연산으로 밸류값을 줄이되, 0일경우 del 명령어로 지워줘야함. pop이나 0의 경우에 value***
    - ***자체가 삭제되지 않아 len에 걸림***
    - target[v] += 1 하려했으나, 초기값 없는 상태에서 target[v] + 1 은 에러 #undefined + 1
        - target.get(value, 0:default) 연산
    
    ```java
    from heapq import heappush
    
    def solution(gems:list)-> list:
        ans = []
        target = {}
        value = len(set(gems))
        left = 0
        for i,v in enumerate(gems):
            target[v] = target.get(v, 0) + 1
            while value == len(target):
                target[gems[left]] -= 1
                if target[gems[left]] == 0:
                    del target[gems[left]] #len 조작하기 위해, - 해서는 키값 자체를 지울수 없음.
                heappush(ans , (i-left,(left+1,i+1)))
                left += 1
        return list(ans[0][1])
    ```
    
- 학습내용
    - heappush 의 자연스러운 사용 (가중치)
    - dictionary(+Counter Class) 학습
    - 한번의 반복문 내에서 left, right 포인터 접근은 좋았으나, 조건부 반복 while문을 조금 더 일찍 생각했었어야 했다.
    - 어렵지 않았는데, 왼쪽을 지우는 로직을 너무 늦게 깨달음
    - ***앞으로 2포인터 문제는 right를 보내고 left를 지우는 순서로 접근해보는 방법을 기억해둔다.***
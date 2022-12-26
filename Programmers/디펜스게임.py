import heapq

def solution(n, k, enemy):
    if k >= len(enemy) :
        return len(enemy)
    answer= []
    res = []
    for index,x in enumerate(enemy) :
        if index < k :
            heapq.heappush(answer, x)
            res.append(x)
        else:
            min_value = heapq.heappop(answer)
            if min_value < x:
                if n - min_value >= 0:
                    # get rid of min_value
                    heapq.heappush(answer,x)
                    n -= min_value
                    res.append(x)
                else :
                    break
            else :
                heapq.heappush(answer,min_value)
                if n - x >= 0:
                    res.append(x)
                    n -= x
                else:
                    break
    return len(res)


"""
### 학습 중점 내용

- 리스트에서 최소 값과 최대값을 뽑아 낼 때 `heapq` 를 쓰냐 안쓰냐가 시간초과에 대해서 가장 큰 역할을 한다.

---

- 이전의 경우 최대값과 최소값을 뽑아 낼 때 다음과 같이 썼다.

```python
list = [1,2,3]

print(min(list)) #1
```

- 그러나 이렇게 할 경우 log(n) 만큼의 성능을 낸다. 시간초과 가능성 존재
- 그래서 heapq 를 써서 표현한다.

```python
import heapq

heapq.heappush(list, value) #insert value
heapq.heappop(list) #pop minimum value

```

- [응용] 최대힙

```python
import heaqp

heapq.heappush(list, (-value, value)) #우선순위 - 로 삽입.
```

- `bisect` 구조체는 이분 탐색으로 하나의 value가 인서트할 때 어느 index에 위치해야 될지 알려줌
    - bisect_left(literable, value)
    - bisect_right(literable, value)
"""
## 두 큐의 합

- 접근
  - 처음 큐의 합을 어떻게 구할까? 
    - ⇒ reduce와 lambda로 빠르게? `reduce(lambda x,y:x+y, nums)`
  - 리턴 조건은 어떻게 될까? 
    - ⇒ q1의 합과, q2의 합이 같으면 그 때의 ans 값
  - 어떻게 균형을 맞출까? 
    - ⇒ q1,q2의 합의 나눈 값을 pivot 잡고 좌우 조절
  - 균형을 맞출수없다면? 
    - ⇒ 뺄게 없으면 -1
  - 시간초과
    1. 두 큐 사이에서 반복적으로 pop insert 되는 경우 , limit를 정해서 -1
    2. queue의 pop(0) 는 Big-O(n) 
        - fluent python을 공부하였을 때 양방향 안전한 deque를 쓰도록 공부하였으나, queue가지고 선입선출..
    
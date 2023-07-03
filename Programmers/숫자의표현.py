from collections import deque
def solution(num:int)->int:
    stack = deque([])
    sum = 0
    cnt = 0
    for i in range(1,num+1):
        while sum+i > num:
                sum -= stack.popleft()
        sum += i
        stack.append(i)
        if sum == num:
            cnt += 1
    return cnt
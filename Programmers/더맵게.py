from heapq import heappush, heappop
def solution(scovile:list , k:int)->int:
    answer = []
    for i in scovile:
        heappush(answer,i)
    cnt = 0
    while answer and answer[0] < k and len(answer) >= 2:
        heappush(answer,heappop(answer) + heappop(answer) * 2)
        cnt += 1
    return cnt if answer[0] >= k else -1
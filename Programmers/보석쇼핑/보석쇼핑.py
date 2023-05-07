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
                # len 조작하기 위해, - 해서는 키값 자체를 지울수 없음.
                del target[gems[left]]
            heappush(ans, (i-left, (left+1, i+1)))
            left += 1
    return list(ans[0][1])
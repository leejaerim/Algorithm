from itertools import combinations
def solution(event:list, banned:list)->int:
    _set = {}
    #문자열 수 및 banned_id에 해당하는지 체크
    for i in banned :
        if _set.get(i) is None:
            _set[i] = (1,[])
        else:
            _set[i] = (_set[i][0]+1, _set[i][1])
        for j in event:
            if len(i) == len(j):
                for k in range(len(j)):
                    if i[k] != '*' and i[k] != j[k]:
                        break
                else:
                    _set[i][1].append(j)
    # dfs 백트래킹
    target = []
    def dfs(keys:list,index:int, ans:list, _set:set,target:list):
        if index > len(keys)-1:
            ans = set(ans)
            if ans not in target:
                target.append(ans)
        else:
            k, next = _set.get(keys[index])
            next = list(set(next))
            for i in ans :
                    if i in next:
                        next.remove(i)
            if k != len(next): # k 값만큼 골라야하는 조합구간
                for i in combinations(next,k):
                    dfs(keys,index+1,ans+list(i),_set,target)
            elif len(next) != 0:
                    dfs(keys,index+1,ans+next,_set,target)
    dfs(list(_set.keys()),0,[],_set,target)
    return len(target)

print(solution(['1b',"eb", 'ab'],['*b',"**"]))



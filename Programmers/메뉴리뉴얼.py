from collections import Counter
from itertools import combinations
def solution(menu:list, course:list)->int:
    ans = {}
    for c in course :
        ans[c] = []
    for i,v in enumerate(menu):
        for j in range(i+1, len(menu)):
            target = set(v) & set(menu[j])
            for c in course:
                for temp in list(combinations("".join(target),c)):
                    temp = "".join(sorted(temp))
                    length = len(temp)
                    if length in ans :
                        ans[length].append(temp)
    answer= []
    for c in course:
        cnt = Counter(ans[c])
        t_max = -1
        for i in cnt.keys():
            t_max = max(t_max, cnt[i])
        for i in cnt.keys():
            if cnt[i] == t_max:
                answer.append(i)
        # for v in ans[c]:
        #     print(v)
            # answer.append("".join(sorted(list(v))))
    return sorted(answer)
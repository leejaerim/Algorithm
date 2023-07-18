from collections import Counter
def solution(s: str)->list:
    target = Counter(s.replace('{','').replace('}','').split(','))
    stack = []
    for i in target:
        stack.append((int(i),target[i]))
    stack.sort(key=lambda x : x[1],reverse=True)
    return [i[0] for i in stack ]

from collections import Counter
def solution(s: str)->list:
    target = Counter(s.replace('{','').replace('}','').split(','))
    return list(map(int,[(k) for k,v in sorted(target.items(), key=lambda x:x[1],reverse=True)]))
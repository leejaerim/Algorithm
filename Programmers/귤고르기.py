from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine).most_common()
    for i,v in counter:
        if k <= 0 :
            return answer
        else:
            k -= v
            answer += 1
    return answer

### Counter 자료구조 및 most_common 메서드.
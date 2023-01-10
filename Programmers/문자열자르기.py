def solution(s):
    answer = 0
    while(len(s) > 0):
        s = for_recur(s)
        answer += 1
    return answer
def for_recur(s:list) -> str:
    counter = 0
    target = ''
    remainder = ''
    for index , char in enumerate(s) :
        if index == 0 :
            target = char
            counter += 1
        else :
            if target == char :
                counter += 1
            else :
                counter -= 1
            if counter == 0 :
                remainder = s[index+1:]
                break
    return remainder

# - 원랜 DFS + 재귀로 깊이 탐색 하려고 하였으나 , remainder 처리  혹은 파라미터 생성 되어야 해서 단순하게 while과 enumerate로 list slice 처리
# - while +  for 반복이라 하더라도,  `O(n)` 수준의 속도 제공한다. (선형 반복)
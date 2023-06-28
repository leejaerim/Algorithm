#stack 사용
def solution(s:str)->bool:
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:#)
            cnt = 1
            while cnt != 0:
                if len(stack) == 0 :
                    return False
                if stack.pop() == '(':
                    cnt -= 1
                else :
                    cnt += 1
    if len(stack) > 0 :
        return False
    return True

#(과 )의 순서에 대한 접근 ) 가 먼저 더 많아질수 없음.
def solution(s:str)->bool:
    cnt = 0
    for i in s:
        if cnt < 0 :
            return False
        if i  == '(':
            cnt += 1
        else:
            cnt -= 1
    return True if cnt == 0 else False
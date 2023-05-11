def isCorrect(s:str)->bool:
    stack = []
    for c in s:
        if c == ')':
            if len(stack) == 0 or stack.pop() != '(' :
                return False
        else:
            stack.append(c)
    return False if len(stack) != 0 else True
def recur(s:str):
    _dict = {'(':0,')':0}
    u,v = "",""
    if s == "":
        return "" # 빈 문자열 -> 빈 문자열
    for idx, char in enumerate(s):
        _dict[char]+=1
        if _dict['('] == _dict[')']:
            u = s[:idx+1]
            v = s[idx+1:]
            break
    if isCorrect(u):
        u += recur(v)
        return u
    else:
        ans = '('
        ans += recur(v)
        ans += ')'
        for i in u[1:-1]:
            if i == '(':
                ans += ')'
            elif i == ')':
                ans += '('
    return ans
def solution(s:str)->str:
    #재귀 필요
    #u,v로 나눌 값 필요. str -> str,str
    return recur(s)
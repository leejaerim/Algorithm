def solution(s):
    close = ["}","]",")"] 
    _dict = {"}":"{","]":"[",")":"("}
    stack = []
    res = 0 
    for x in range(len(s)):
        flag = True
        target = s[x:] + s[:x]
        for y in target :
            if y in close:
                if len(stack) == 0 or _dict[y] != stack.pop():
                    flag = False
                    break
            else:
                stack.append(y)
        if len(stack) != 0 :
            flag = False
        if flag == True:
            res += 1
    return res
            
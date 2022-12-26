def solution(s):
    if len(s) % 2 == 1:
        return 0
    stack = []
    for x in s:
        if len(stack) == 0:
            stack.append(x)
        else:
            target = stack.pop()
            if target != x :
                stack.append(target)
                stack.append(x)
    if len(stack) == 0 :
        return 1
    else :
        return 0
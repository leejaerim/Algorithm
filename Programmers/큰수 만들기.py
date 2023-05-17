#stack을 이용해서 k 만큼 길이 관리를 할 수 있는지 여부 중요.

def solution(number:str , k:int)->str:
    stack = []
    number = list(map(lambda x:int(x),number))
    popcnt = 0
    for i in number :
        if len(stack) == 0:
            stack.append(i)
        else:
            while stack:
                target = stack.pop()
                if i <= target or popcnt == k:
                    stack.append(target)
                    break
                else:
                    popcnt += 1
            stack.append(i)
    while popcnt != k :
        stack.pop()
        popcnt+=1
    stack = list(map(lambda x:str(x),stack))
    return "".join(stack)
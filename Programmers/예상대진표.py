def solution(n:int, a:int, b:int)->int:
    stack = list(map(lambda x: 1 if x == (a-1) or x == (b-1) else 0, range(n)))
    answer = 0
    while True:
        temp_stack = []
        answer += 1
        i = 0
        while i < n:
            if stack[i] != 0 and stack[i+1] != 0:
                return answer
            if stack[i] != 0:
                temp_stack.append(stack[i])
            elif stack[i+1] != 0:
                temp_stack.append(stack[i+1])
            else:
                temp_stack.append(0)
            i+=2
        stack = temp_stack
        n = len(stack)
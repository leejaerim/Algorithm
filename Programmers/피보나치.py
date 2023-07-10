def solution(n):
    # stack = [0,1]
    # if n < 2 :
    #     return stack[n]
    # while len(stack) <= n :
    #     stack.append((stack[-1] + stack[-2])% 1234567)
    a,b = 0, 1
    for i in range(0,n):
        a, b = b, (a+b)%1234567
    return a
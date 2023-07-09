from collections import Counter
# 접근방법
# 1. 숫자 하나에 대한 최소 공배수를 구함
# 2. 최소 공배수의 집합들을 카운트함
# 3. 가장 많은 갯수의 수로 곱함

def lcm(n:int)->list:
    i = 2
    stack = []
    while n != 1 :
        while n % i == 0:
            n = n // i
            stack.append(i)
        i += 1
    return stack
def solution(arr:list)->list:
    cnt = {}
    answer = 1
    for i in arr:
        targets = Counter(lcm(i))
        for target in targets:
            if not target in cnt:
                cnt[target] = targets[target]
            else:
                cnt[target] = max(cnt[target] , targets[target])
    for target in cnt:
        answer *= (target ** cnt[target])
    return  answer
# 더 쉬운 접근
# 유클리드 호제법을 이용해서 gcd를 구하면 lcm도 편하게 구할수 있다.
# gcd와 lcm은 바로바로 쓸 수 있도록 이해하고 넘어가자.

def lcm(a:int,b:int)->int:
    return (a*b) // gcd(a,b)
def gcd(a:int,b:int)->int:
    while(b):
        a,b = b, a%b
    return a
def solution(arr:list)->list:
    target = None
    for i in arr:
        if target is None :
            target = i
        else:
            target = lcm(target,i)
    return  target
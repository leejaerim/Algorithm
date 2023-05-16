#case 1:
def solution(k:int, d:int)->int:
    x = 0
    ans = []
    while x * k <= d:#x 증가.
        y = 0
        while y*k <= d:
            if pow((x*k),2) + pow((y*k),2) <= pow(d,2):
                ans.append((x*k,y*k))
            y += 1
        x += 1
    return len(ans)
# time out O(n^2)

#case 2:
def solution(k:int, d:int)->int:
    x = 0
    ans = []
    while x * k <= d:#x 증가.
        y = x
        while y*k <= d:
            if pow((x*k),2) + pow((y*k),2) <= pow(d,2):
                ans.append((x*k,y*k))
            y += 1
        x += 1
    #filter 사용해서, 1사분면의 y=x축의 절반만 구한뒤 반대 값 +
    return len(ans) + len(list(filter(lambda x:x[0]!=x[1],ans)))
# time out O(nlogn)

#case 3:
from itertools import product
def solution(k:int, d:int)->int:
    test = list(filter(lambda x:pow(k*x,2)<=pow(d,2), range(d+1)))
    temp2 = list(filter(lambda x:(pow(x[0]*k,2) + pow(x[1]*k,2)) <= pow(d,2),product(test, test)))
    return len(temp2)
# time out O(N^2) product multiple.

#case 4 :
def solution(k:int, d:int)->int:
    ans = 0
    for y in range(0,d+1,k):
        ans += ((d**2-y**2)**0.5)//k+1

    return int(ans)
#solution

#case 5 :
def solution(k:int, d:int)->int:
    return int(sum(list(map(lambda x:((d**2-x**2)**0.5)//k+1,range(0,d+1,k)))))
#lambda solution
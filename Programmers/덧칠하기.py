def solution(n,m,section)->int:
    ans = 0
    gap = 0
    for i in section :
        if i > gap :
            if i + m - 1 < n:
                gap = i + m - 1
            else:
                ans+=1
                break
            ans+=1
    return ans
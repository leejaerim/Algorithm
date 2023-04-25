def solution(n):
    memo = [0,1,2,3]
    last = 4
    while last <= n :
        memo.append((memo[last-2] + memo[last-1])%1000000007)
        last = len(memo)
    return memo[n]
def solution(n):
    memo = [0,1,2]
    if n < 3 :
        return memo[n]
    i = 3
    while(i <= n):
        memo.append((memo[i-1] + memo[i-2]) %1234567)
        i += 1
    return memo[n]

# 피보나치
# 메모라이징
# 재귀로 풀었으나, 런타임 에러. (과도한 재귀 최대 2000)
def solution(n):
    ans = ""
    while n > 0:
        target = n % 3
        n = n // 3
        if target == 0:
            ans = "4" + ans
            n = n-1
        else:
            ans = str(target) + ans
    return ans

# target이 0 일때, n-1 빼는 이유를 이해하는 것이 중요하다.
# 50,000,000 의 제한에서는  log,pow와 같은 방법을 통해 y=x 이상의 기울로 알고리즘을 풀어야 한다. (효율성 이슈)
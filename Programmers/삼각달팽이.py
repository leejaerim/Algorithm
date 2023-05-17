def solution(n:int)->list:
    test = [[0 for i in range(n)] for i in range(n)]
    if n ==1 :
        return [1]
    i , j = 0 , 0
    test[i][j] = 1
    cnt = 1
    while True:
        #조건
        while i+1 != n and test[i+1][j] == 0: #down
            cnt += 1
            i += 1
            test[i][j] = cnt
        while j+1 != n and test[i][j+1] == 0:
            cnt += 1
            j += 1
            test[i][j] = cnt
        while i-1 > 0 and j-1 > 0 and test[i-1][j-1] == 0:
            cnt += 1
            i -= 1
            j -= 1
            test[i][j] = cnt
        if i+1 == n or test[i+1][j] != 0:
            break

    ans = []
    for i in test :
        ans += filter(lambda x:x!=0,i)
    return ans
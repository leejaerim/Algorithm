from collections import Counter
def solution(weights:list)->int:
    ans = 0
    cnt = Counter(weights)
    #1배, 2배 1,5배 ,1.33배만 검색합니다.
    #즉, 본인보다 큰 값만 체크 합니다.
    for i in cnt.keys():
        if cnt[i] > 1 :
            #중복없는 조합 : nC2 (n)*(n-1) // 2 * 1
            ans += cnt[i] * (cnt[i]-1)//2
        if i * 2 in cnt :
            ans += cnt[i*2] * cnt[i]
        #1.5배 1.333배의 경우 정수일 경우에만 연산합니다.
        if i *3 % 2 ==0 and i*3//2 in cnt :
            ans += cnt[i*3//2] * cnt[i]
        if i *4%3==0 and i*4//3 in cnt :
            ans += cnt[i*4//3] * cnt[i]
    return ans
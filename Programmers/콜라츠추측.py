def solution(k, ranges):
    answer = []
    idx = 0
    exp = [(idx,k)] #x,y좌표
    area = [] #너비
    while k != 1 :
        temp = k
        if k % 2 == 0 : #짝
            k = k/2
        else: #홀
            k = 3*k+1
        area.append((temp + k)/2) #너비 계산
        idx+=1
        exp.append((idx,k))
    length = len(exp)-1
    #범위별, 총 면적 계산
    for range in ranges:
        x,xa = range
        xa = length + xa
        if xa < x :
            answer.append(-1.0)
        else:
            answer.append(sum(area[x:xa]))
    return answer
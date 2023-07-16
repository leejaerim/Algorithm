def solution(clothes)->list:
    dix = {}
    for target, kind in clothes:
        if not kind in dix :
            dix[kind] = [target]
        else:
            dix[kind].append(target)
    answer = 1
    #각 의상의 종류에서 1개를 고르거나, 0개를 고르는 것을 추출한 뒤, 각 경우의 수를 의상의 종류마다 곱한다.
    #최종 값에서 모든 의상 종류에서 의상을 고르지 않는 경우인 1가지를 제외한 값이 정답.
    for target in dix.values():
        answer *= (len(target)+1)
    return answer - 1
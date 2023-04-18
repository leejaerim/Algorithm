def solution(missiles:list)->int:
    missiles.sort(key=lambda x : (x[0],x[1]))
    # 첫번째 배열의 값과 두번째배열의 값으로 리스트를 정렬하는 것이 중요하며, 람다를 통해 구현할 줄 알아야한다.
    target = 0
    for s,e in missiles:
        if target == 0:
            prevs, preve = s,e
            target += 1
        else :
            if s < preve :
                if e < preve:
                    prevs, preve = s,e
            else:
                prevs, preve = s,e
                target += 1
    return target
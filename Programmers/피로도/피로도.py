from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for i in list(permutations(dungeons,len(dungeons))):
        target = k
        temp = 0
        for minhp, hp in i:
            if target >= minhp:
                target -= hp
                temp += 1
        answer = max(answer,temp)
    return answer

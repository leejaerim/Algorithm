def solution(picks, minerals):
    return recur(picks,minerals,0)
def recur(picks, minerals, stamina):
    if len(minerals) < 1 or (picks[0] == 0 and picks[1] == 0 and picks[2] ==0):
        return stamina
    a = 9999
    if picks[0] > 0:
        a = min(a,recur([picks[0]-1, picks[1], picks[2]], minerals[5:],stamina + get_minerals("dia", minerals[:5])))
    if picks[1] > 0:
        a = min(a,recur([picks[0], picks[1]-1, picks[2]],minerals[5:],stamina + get_minerals("iron", minerals[:5])))
    if picks[2] > 0:
        a = min(a,recur([picks[0], picks[1], picks[2]-1],minerals[5:],stamina + get_minerals("stone", minerals[:5])))
    return a

def get_minerals(pick, minerals)->int:
    res = 0
    if len(minerals) == 0:
        return 0
    if pick == "dia":
        res =  len(minerals)
    elif pick == "iron" :
        for i in minerals :
            if i == "diamond":
                res += 5
            else :
                res += 1
    else :
        for i in minerals :
            if i == "diamond":
                res += 25
            elif i == "iron" :
                res += 5
            else:
                res += 1
    return res
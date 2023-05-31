def solution(n):
    ans = []
    def hanoi(node, _from, _to, _aux):
        if node == 1 :
            ans.append([_from,_to])
        else :
            hanoi(node-1,_from,_aux,_to)
            ans.append([_from,_to])
            hanoi(node-1,_aux,_to,_from)
    hanoi(n,1,3,2)
    return ans
solution(2)
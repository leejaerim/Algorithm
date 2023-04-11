def solution(seq:list, k:int)->list:
    answer = []
    sum = 0
    left = 0
    _len = len(seq)
    minimum = len(seq)
    if k in seq :
        return [seq.index(k),seq.index(k)]
    seq.reverse()
    for i,v in enumerate(seq):
        right = i
        sum += v
        if sum >= k :
            if sum == k and right - left <= minimum:
                minimum = right - left
                answer = [ _len-1-right,_len-1-left]
            sum -= seq[left]
            left += 1
    return answer
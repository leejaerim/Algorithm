from heapq import heappush
def solution(seq:list , k:int)->list:
    left, right = 0 , 0
    sum = seq[0]
    ans = []
    # right 를 어떻게 끝까지
    while right < len(seq):
        if sum > k:
            sum -= seq[left]
            left +=1
        elif sum == k :
            heappush(ans, (right-left,(left,right)))
            right+= 1
            if right < len(seq):
                sum += seq[right]
        else :#sum<k
            right += 1
            if right < len(seq):
                sum += seq[right]
    return list(ans[0][1])
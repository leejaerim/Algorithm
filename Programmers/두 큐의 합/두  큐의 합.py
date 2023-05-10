def solution(q1:list, q2:list)->int:
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    target = int((q1_sum + q2_sum)/2)
    answer = 0
    while q1_sum != q2_sum:
        if target > q1_sum :
            temp = q2.pop(0)
            q1.append(temp)
            q1_sum += temp
            q2_sum -= temp
        else :
            temp = q1.pop(0)
            q2.append(temp)
            q2_sum += temp
            q1_sum -= temp
        answer += 1
        if q1_sum == 0 or q2_sum == 0 :
            return -1
    return answer
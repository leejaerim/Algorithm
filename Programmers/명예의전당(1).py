import heapq

def solution(k, score):
    answer = []
    list_master_piece = []
    for i in score :
        if len(list_master_piece) < k  :
            heapq.heappush(list_master_piece,i)
        else:
            if i > list_master_piece[0] :
                heapq.heappop(list_master_piece)
                heapq.heappush(list_master_piece, i)
        answer.append(list_master_piece[0])
    return answer


# - heapq를 사용했다. 매번 잊어 먹는 것 같아서 다시 정리한다.
#     - `heappush(list, value)`
#     - `heappop(list)`
#     - `list[0]`  최소값.
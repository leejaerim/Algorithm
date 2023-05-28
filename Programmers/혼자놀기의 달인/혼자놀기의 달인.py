def solution(cards:list)->int:
    isOpend = [0] * len(cards) #isOpend = list(map(lambda x : 0, range(len(cards))))
    ans = []
    for i in range(len(isOpend)):
        temp = []
        j = i
        while isOpend[j] == 0:
            isOpend[j] = 1
            temp.append(cards[j])
            j = cards[j] - 1
        if temp : ans.append(len(temp))
    if len(ans) <= 1 : return 0
    ans = sorted(ans,reverse=True)
    return ans[0]*ans[1]
solution([8,6,3,7,2,5,1,4])
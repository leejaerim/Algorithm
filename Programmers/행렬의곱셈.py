def solution(arr1:list, arr2:list)->list:
    answer= []
    for j in range(len(arr1)):
        target= []
        for i in range(len(arr2[0])):
            temp = 0
            for h in range(len(arr2)):
                temp += (arr1[j][h] * arr2[h][i])
            target.append(temp)
        answer.append(target)
    return answer
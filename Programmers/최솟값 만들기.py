def solution(list1:list, list2:list)->int:
    list1.sort(reverse=True)
    list2.sort()
    total = 0
    for i in range(len(list1)):
        total  = total + list1[i] * list2[i]
    return total
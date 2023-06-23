def solution(files:list)->int:
    answer = []
    for file in files:
        flag = True
        tailFlag = True
        head = ''
        tail = ''
        number = ''
        for char in file:
            if char.isnumeric() and tailFlag:
                flag = False
                number += char
            else:
                #처음
                if flag :
                    head += char
                #
                else:
                    tailFlag = False
                    tail += char
        answer.append((head,int(number),tail,file))
    answer.sort(key=lambda x : x[1])
    answer.sort(key=lambda x : x[0].lower())
    return [file[3] for file in answer]
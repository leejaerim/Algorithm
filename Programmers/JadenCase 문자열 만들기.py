def solution(s):
    answer = []
    flag = True
    for i in s:
        if i == ' ':
            answer.append(i)
            flag = True
        else:
            if i.isalpha() and flag:
                answer.append(i.upper())
            else:
                answer.append(i.lower())
            flag = False
    return ''.join(answer)


def solution(s):
    answer = []
    for idx,i in enumerate(s.lower()):
        answer.append(i.upper()) if i.isalpha() and (s[idx-1] == ' ' or idx == 0) else answer.append(i)
    return ''.join(answer)
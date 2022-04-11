# 문제명 : 음양 더하기
# 사이트 : https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3

def solution(absolutes, signs):
    answer = 0
    for i in range(0,len(absolutes)):
        if signs[i]:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    return answer

# 쉬운 문제.
# 다만 range 보다 zip 이라는 내장 함수를 써서 간결 쉽게 푼 사람이 많았다.
# 참고 :  for absolute,sign in zip(absolutes,signs)
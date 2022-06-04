#https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3
#제약사항
##1 ≤ s의 길이 ≤ 50
##s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
##return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

def solution(s):
    answer = 0
    s = s.replace("zero","0").replace("one","1").replace("two","2").replace("three","3").replace("four","4").replace("five","5").replace("six","6").replace("seven","7").replace("eight","8").replace("nine","9")
    answer = int(s)
    return answer
#Problem : https://programmers.co.kr/learn/courses/30/lessons/42888
#딕셔너리 자료구조를 사용해서 O(n) 만큼의 성능
#python에서 is는 객체 판단, == 값 판단을 한다.

def solution(record):
    answer = []
    user = {}
    for i in record:
        arr = list(i.split(" "))
        if arr[0] != "Leave" :
            user[arr[1]] = arr[2]
    for i in record:
        arr = list(i.split(" "))
        if arr[0] == "Enter":
            answer.append(f"{user.get(arr[1])}님이 들어왔습니다.")
        elif arr[0] == "Leave":
            answer.append(f"{user.get(arr[1])}님이 나갔습니다.")
    return answer




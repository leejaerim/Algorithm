def solution(map:list)->int:
    stack = []
    ans = []
    key = 0
    for target in map :
        #보조 컨테이너 존재하면 => 빼서 넣기(단, 중복되는 박스 넘버는 없음.제한사항 참고)
        if target in stack:
            item = stack.pop()
            if target == item :
                ans.append(item)
            else:
                return len(ans)
        else:
            for i in range(key+1,len(map)+1):
            #삽입할 수 있는 방법은 두가지
            # 1 : 정방향으로 넣기
                if i == target : # 타입은 int
                    ans.append(target)
                    key = i
                    break
                # 2 : 보조컨테이너를 빌려 넣기
                else :
                    stack.append(i)

    return len(ans)
# 문제명 : 색종이
# 사이트 : https://www.acmicpc.net/problem/2590
import random;



def function_test(paper) -> (int):

    ans = 0
    #for _ in range(6):
        #paper.append(int(input()))
    if paper[6]:
        ans += paper[6]

    while paper[5]:
        area = 36 - 5*5
        paper[5] -= 1
        paper[1] = max(paper[1]-area, 0)
        ans += 1

    while paper[4]:
        area = 36 - 4*4
        area -= min(paper[2], 5) * 4
        paper[4] -= 1
        paper[2] = max(paper[2]-5, 0)
        paper[1] = max(paper[1]-area, 0)
        ans += 1

    while paper[3]:
        area = 36 - 9 * min(paper[3], 4)
        if paper[3] >= 4:
            paper[3] -= 4
            area = 0
        elif paper[3] == 3:
            area -= min(1, paper[2]) * 4
            paper[3] -= 3
            paper[2] = max(paper[2]-1, 0)
        elif paper[3] == 2:
            area -= min(3, paper[2]) * 4
            paper[3] -= 2
            paper[2] = max(paper[2]-3, 0)
        else:
            area -= min(5, paper[2]) * 4
            paper[3] -= 1
            paper[2] = max(paper[2]-5, 0)

        paper[1] = max(paper[1]-area, 0)
        ans += 1

    while paper[2]:
        area = 36 - 4 * min(paper[2], 9)
        paper[2] = max(paper[2]-9, 0)
        paper[1] = max(paper[1]-area, 0)
        ans += 1

    while paper[1]:
        paper[1] = max(paper[1]-36, 0)
        ans += 1

    return ans

def chkNum(list) -> (int):
    # 1과 5을 가지고 6을 만드는 과정
    cnt = list[4]
    for i in range(0,cnt):
        if list[0] >= 11:
            list[0] -= 11
            list[4] -= 1
            list[5] += 1
        else:
            list[0] = 0
            list[5] += list[4]
            list[4] = 0
            break
    #2와 4를 가지고 6을 만드는 과정
    cnt = list[3]
    for i in range(0,cnt):
        if list[1] >= 5:
            list[1] -= 5
            list[5] += 1
            list[3] -= 1
        else:
            while list[0]>=4 and list[1] <5:
                list[0] -= 4
                list[1] += 1
            if list[1] == 5 :
                list[1] -= 5
                list[5] += 1
                list[3] -= 1
                while list[0] >= 20 and list[3] >0:
                    list[0] -= 20
                    list[3] -= 1
                    list[5] += 1
                if list[3] == 0 :
                    break
                elif list[0] < 20:
                    list[0] = 0
                    list[5] += list[3]
                    list[3] = 0
            elif list[0] < 4:
                list[0] = 0
                list[1] = 0
                list[5] += list[3]
                list[3] = 0
            break

    cnt = list[2]
    # 3을가지고 6 만드는 과정
    while list[2] > 0:
        if list[2] >= 4 :
            list[2] -= 4
            list[5] += 1
        else:
            if list[0] >= 7 and list[1] >= 5:
                list[0] -= 7
                list[1] -= 5
                list[2] -= 1
                list[5] += 1
            elif list[0] >= 5 and list[1] > 0:
                list[1] -= 1
                list[0] -= 5
                list[2] += 1
            else :
                if list[1] <= 0:
                    if list[0] >= 9 :
                        list[0] -= 9
                        list[2] += 1
                    elif list[0] >= 4:
                        list[0] -= 4
                        list[1] += 1
                    else:
                        list[0] = 0
                        list[2] = 0
                        list[5] += 1
                elif list[0] < 5:
                    if list[1] >= 9:
                        list[1] -= 9
                        list[5] += 1
                    elif list[1] > 4: # list[2]가 1장
                        list[1] -= 5
                        list[2] -= 1
                        list[0] -= 7
                        list[5] += 1
                    elif list[1] > 3: # list[2]가 1장
                        list[1] -= 5
                        list[2] -= 1
                        list[0] -= 7
                        list[5] += 1
                    elif list[1] > 1 :#list[2]가 2장
                        list[1] -= 3
                        list[0] -= 6
                        list[2] -= 2
                        list[5] += 1
                    else:
                        list[1] -= 1
                        list[0] -= 5
                        list[2] -= 3
                        list[5] += 1

    while list[1] > 0 :
        if list[1] >= 9:
            list[1] -= 9
            list[5] += 1
        elif list[0] >= 4:
            list[0] -= 4
            list[1] += 1
        else :
            list[0] = 0
            list[1] = 0
            list[5] += 1
    while list[0] > 0:
        if list[1] < 0:
            list[0] += list[1]*4 
        else:
            list[0] -= 36
            list[5] += 1
    return list[5]


def test():
    list = []
    ans = []
    for i in range(0,6):
    #list.append(int(input()))
        list.append(random.randint(0,10000))
    paper = [0]
    for i in list:
        paper.append(i)
        ans.append(i)
    if not chkNum(list)  == function_test(paper) :
        print(ans)



for i in range(0,1000):
    test()
#print(chkNum([7, 5, 1, 0, 0, 0]))
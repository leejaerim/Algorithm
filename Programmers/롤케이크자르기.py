from collections import Counter
def solution(topping):
        ans = 0
        first_flag = False
        second_flag = False
        left = Counter(topping[:0])
        right = Counter(topping[0:])
        for i in range(0,len(topping)):
                left[topping[i]] += 1
                if right[topping[i]] == 1:
                        del right[topping[i]]
                else :
                  right[topping[i]] -= 1
                if len(left) == len(right) :
                        first_flag =True
                        second_flag = True
                        ans+=1
                else :
                     first_flag = False
                if first_flag == False and second_flag == True:
                        break
        return ans
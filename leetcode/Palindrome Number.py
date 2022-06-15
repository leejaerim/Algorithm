#9. Palindrome Number
#My Answer
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else :
            res = list(str(x))
            len_res = len(res)
            for i in range(len_res):
                if res[i] != res[len_res-i-1]:
                    return False
            return True

#Best Answer i think :
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
#Point :
#reverse List using slice 
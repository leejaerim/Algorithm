class Solution:
    def longestPalindrome(self, s: str) -> int:
        isChecked = True 
        res = 0
        Added = []
        for i in s:
            if not i in Added :
                Added.append(i)
                num = s.count(i)
                if num % 2 == 0:
                    res += num
                else:
                    if isChecked :
                        res += num
                        isChecked = False
                    else :
                        res = res + num -1
        return res
                
                
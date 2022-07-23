class Solution:
    def isPalindrome(self, x: str) -> bool:
        if x ==  "" :
            return False
        else :
            res = list(x)
            len_res = len(res)
            for i in range(len_res):
                if res[i] != res[len_res-i-1]:
                    return False
            return True
    def longestPalindrome(self, s: str) -> str:
        lengthOfStr = len(s) 
        if lengthOfStr == 1 : 
                return s
        for i in range(lengthOfStr,0,-1):
            # i == length of between two str
            for j in range(0,lengthOfStr-i+1): 
                if self.isPalindrome(s[j:j+i]):
                    return s[j:j+i]
        return s[0]
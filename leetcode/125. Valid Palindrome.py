class Solution:
    def isPalindrome(self, s: str) -> bool:
        for k in s:
            if not k.isalnum():
                s = s.replace(k,"")
        lens = len(s)
        s = s.lower()
        for i in range(lens):
            if s[i] != s[lens-i-1]:
                return False
        return True

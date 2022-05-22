class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        for i in s.split():
            string = ""
            for j in i:
                string = j + string
            res = res + " " +string
        return res[1:]
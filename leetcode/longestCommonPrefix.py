class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min = 201
        for i in strs:
            if len(i) < min:
                min = len(i)
        for j in range(min):
            prefix = strs[0][j]
            for i in range(len(strs)):
                if prefix == strs[i][j]:
                    check = True
                else:
                    check = False
                    break
            if check :
                res  += prefix
            else :
                break
        return res
        

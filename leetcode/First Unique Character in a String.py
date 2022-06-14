# 387. First Unique Character in a String
#My Answer :
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,j in enumerate(s):
            if s.count(j) < 2 :
                return i
        return -1

# Best Answer i think :
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i, ele in enumerate(s):
#             if ele not in s[i+1:] + s[:i]:
#                 return i
#         return -1
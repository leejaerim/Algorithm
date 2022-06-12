#242. Valid Anagram
#My Answer:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        for i in s:
            if s.count(i) != t.count(i):
                return False
        return True

#Best Answer i think :
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return collections.Counter(s) == collections.Counter(t)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return((format(n,"b")).count('1'))

### another answer 
#        return [_ for _ in str(bin(n))].count("1")

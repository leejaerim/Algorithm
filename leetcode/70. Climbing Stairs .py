#70. Climbing Stairs 
# Using Dynamic Programming & Memorizing
class Solution:
    memo =  [0,1,2,3] + [0]*42
    def climbStairs(self, n: int) -> int:
        if n < 3 :
            return self.memo[n]
        if self.memo[n] != 0:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]
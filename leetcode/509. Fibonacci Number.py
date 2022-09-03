class Solution:
    def fib(self, n: int) -> int:
        memo = [0] * 31
        if n == 0 or n == 1 :
            memo[n] = n
            return n
        else :
            if  memo[n] != 0:
                return memo[n]
            else:
                memo[n] = self.fib(n-1) + self.fib(n-2)
                return memo[n]
# Using Memorizing                
class Solution:
    def fib(self, n: int) -> int:
        memo = [0,1,]
        for i in range(2,n+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[n]
                
                
class Solution:
    res = [0,0]
    def helper(self, cost : List[int] , target : int) -> int:
        try :
            return self.res[target]
        except: 
            for i in range(2,target):
                self.res.append(self.helper(cost,i-1) +cost[i-1] if self.helper(cost,i-1) + cost[i-1] <= self.helper(cost,i-2) + cost[i-2] else self.helper(cost,i-2) + cost[i-2])     
            return (self.res[target-1])
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.res = [0,0]
        return self.helper(cost,len(cost)+1)
        
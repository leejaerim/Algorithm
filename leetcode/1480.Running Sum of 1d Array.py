class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [] 
        sum_res = 0 
        for i in nums:
            sum_res += i
            res.append(sum_res)
        res = {}
        return res
    
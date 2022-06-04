#1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,k in enumerate(nums) :
            if nums[i+1:].count(target - k):
                return [i,nums[i+1:].index(target-k)+i+1]
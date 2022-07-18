class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lists = list(set(nums))
        max = 0
        res = 0
        for i in lists:
            tmp = nums.count(i)
            if max < tmp:
                max = tmp
                res = i 
        return res
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0
        temp = -101
        for i,k in enumerate(nums):
            if temp == k:
                nums[i] = 101
            else :
                res+=1
            temp = k
        nums.sort()
        return res


# BestAnswer i think:
# nums[:] = sorted(set(nums))
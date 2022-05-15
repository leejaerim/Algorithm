from winreg import EnumValue


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i,k in enumerate(nums):
            nums[i] = k*k
        nums.sort()
        return nums
a = Solution()
a.sortedSquares([-4,-1,0,3,10])
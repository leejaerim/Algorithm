class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
            nums.insert(0,nums.pop())
a = Solution()
testcase1 = [1,2,3,4,5,6,7]
a.rotate(testcase1,4)
print(testcase1)
#best answer
#         k %= len(nums)
#         nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
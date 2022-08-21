
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        left_sum = 0
        right_sum = sum(nums[1:])
        while (pivot >= 0 and pivot != len(nums) ):
            if left_sum != right_sum:
                    left_sum += nums[pivot]
                    if pivot+1 == len(nums):
                        return -1
                    right_sum -= nums[pivot+1]
                    pivot  += 1
            else:
                if nums[pivot] == 0:
                    if pivot == 0 :
                        return 0
                    while(nums[pivot-1] == 0):
                        pivot -= 1
                return pivot
        return -1
    #best answer i think
    def pivotIndex2(self, nums: List[int]) -> int:
        totals = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            if leftsum == (totals - nums[i] - leftsum):
                return i
            leftsum += nums[i]
        return -1
# runtime complexity : O(log n)
# 정렬된 리스트 기준으로 Binary Search 할 수 있다.
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        right = len(nums)-1
        left = 0
        while(left <= right):
            mid = (right + left) //2
            if nums[mid] == target: return mid
            elif  nums[mid] < target :
                left = mid + 1
            else :
                right = mid - 1
        return -1
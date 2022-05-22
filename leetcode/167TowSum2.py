class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0,len(numbers)):
            if target-numbers[i] in numbers[i+1:] :
                j = numbers[i+1:].index(target-numbers[i]) 
                return [i+1,i+j+2]
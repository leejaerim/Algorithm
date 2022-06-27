class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            digits[-1] = 0
            try:
                digits[:-1] = self.plusOne(digits[:-1])
            except:
                return [1]+digits
        else:
            digits[-1] += 1
        return digits
        
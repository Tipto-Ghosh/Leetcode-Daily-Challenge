from typing import List 

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)
        
        while original in nums_set:
            original *= 2
        
        return original


sol = Solution()
print(sol.findFinalValue(nums = [5,3,6,1,12], original = 3))
print(sol.findFinalValue([2,7,9] , 4))